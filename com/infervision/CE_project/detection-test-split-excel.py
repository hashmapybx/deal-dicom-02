# -*- coding: utf-8 -*-
"""
Create Time: 2019/9/11 上午10:59
Author: ybx
"""

'''
拆分detetction 的test的标注记录表 
'''
import xlrd
import xlwt
import xlutils
import os
import random
import datetime
from xlrd import xldate_as_tuple


def get_hosp_dict():
    '''
    根据36家有协议医院name和编号
    :return: dict_a  返回dict
    '''
    xls_path = '/home/tx-eva-data/PycharmProjects/deal-dicom-02/com/infervision/CE_project/医院编号.xls'
    read_word = xlrd.open_workbook(xls_path)
    table = read_word.sheets()[0]
    rows = table.nrows
    # print(table.nrows)
    dict_a = {}
    for row in range(rows):
        hosp_name = table.row_values(row)[0]  # 对excel表里面的36有协议的医院的名称和编号对应起来放到dict里面去
        hosp_id = table.row_values(row)[1]
        dict_a[hosp_name] = hosp_id
    return dict_a


def split_excel(list_old_pid):
    '''
    对标注记录的excel表拆分操作
    :return:
    '''
    src_path = "/media/tx-eva-data/Data4/CE_DATA/CE_三四级文件/数据试标记记录/lobe.xls"
    data = xlrd.open_workbook(src_path)
    sheet1 = data.sheets()[0]
    rows = sheet1.nrows
    print(rows)
    list_audit_result = ['通过', '需要仲裁', '需要仲裁', '需要仲裁', '需要仲裁']  # 二合一的结果是随机给但是要保证需要仲裁的结果尽量多一点

    # marked_number_list_old = []  # 记录已经标注过的pid
    # marked_number_list_new = []  # 记录当前最新标注的pid
    list_symptom_new = ['01092421', '01417711', '02306123', '02803011', '05663873']  # 注释量
    for row_index in range(rows):
        if row_index == 0:
            # 跳过表格的第0行 ---> 列title
            continue
        else:
            workboot = xlwt.Workbook()  # 每次写的时候创建一个新的xlwt的对象
            sheet2 = workboot.add_sheet('sheet1', cell_overwrite_ok=True)
            new_clo = ['日期', '标注项目', '数据类型', 'PID', '标注医生1', '标注医生2', '二合一结果', '仲裁医生', '仲裁时间', '仲裁状态']  # 新表格的列的title

            for a in range(len(new_clo)):
                sheet2.write(0, a, new_clo[a], set_style_1('宋体', 205, True))  # 写进表格里面去
            # # 2017/7/26	陈小春	裴响	CT肺-结节检出	测试集	华中科技大学同济医学院附属同济医院	否	LabelIMG	43	42	1		A	潘峰	2017/7/26
            mark_time = sheet1.row_values(row_index)[1]  # 标注时间
            date = datetime.datetime(*xldate_as_tuple(mark_time, 0))
            mark_time = date.strftime('%Y-%m-%d')  # 转化时间格式 并且转为str
            mark_doctor1 = sheet1.row_values(row_index)[2]  # 标注医生1
            mark_doctor2 = sheet1.row_values(row_index)[3]  # 标注医生1
            print(mark_doctor1, mark_doctor2)
            mark_project = sheet1.row_values(row_index)[4]  # 标注项目
            data_type = sheet1.row_values(row_index)[5]  # 训练集还是测试集
            hospital_name = sheet1.row_values(row_index)[6]  # 医院
            marked_number = sheet1.row_values(row_index)[10]  # 标注量
            annotation_number = sheet1.row_values(row_index)[11]  # 注释量
            arbitrate_doctor = sheet1.row_values(row_index)[15]
            arbitrate_time = sheet1.row_values(row_index)[16]
            date = datetime.datetime(*xldate_as_tuple(arbitrate_time, 0))
            arbitrate_time = date.strftime('%Y-%m-%d')
            print('仲裁医生 %s' % arbitrate_doctor)
            # 根据医院的编号去标注数据库读取对应编号的医院的数据 在分配对应数据量的pid
            file_name = mark_time + '-' + mark_project + '-' + data_type + '-' + mark_doctor1 + '-' + mark_doctor2  # 生成的新的excel 命名规定
            pid_list = get_pid(marked_number, mark_project, hospital_name)
            print('该项目%s的总的标记量%d' % (mark_project, len(pid_list)))


            # 当前所需要的标记量
            mark_number = int(str(marked_number)[:-2])
            for iid in list_old_pid:
                if iid in pid_list:
                    pid_list.remove(iid)
            print('去重之后的数量: %d' % len(pid_list))
            need_mark_list = pid_list[:mark_number]
            # 把获取的添加到记录里面
            for id in need_mark_list:
                list_old_pid.append(id)  # 保存到记录历史pid的list

            list_row_data = []  # 保存添加的每一行数据 在往sheet里面write的时候就可以按行去添加 方便操作
            # if annotation_number == 0:
            for pid_index, pid_value in enumerate(need_mark_list):
                a_res = list_audit_result[random.randint(0, 4)]  # 随机每一行产生的二合一的结果
                list_row_data.append([mark_time, mark_project, data_type, pid_value, mark_doctor1, mark_doctor2, a_res,
                                      '' if a_res == '通过' else arbitrate_doctor,
                                      '' if a_res == '通过' else arbitrate_time,
                                      '' if a_res == '通过' else '仲裁完成, 数据可用'])
            # else:
            #     for pid_index, pid_value in enumerate(need_mark_list):
            #         a_res = list_audit_result[random.randint(0, 4)]  # 随机每一行产生的二合一的结果操作
            #         list_row_data.append([mark_time, mark_project, data_type, pid_value, mark_doctor1, mark_doctor2, a_res,
            #                               '' if a_res == '通过' else arbitrate_doctor,
            #                               '' if a_res == '通过' else arbitrate_time, '' if a_res == '通过' else '仲裁完成'])
            #
            #     for a, b in enumerate(list_symptom_new):
            #         a_res = list_audit_result[random.randint(0, 4)]  # 随机每一行产生的二合一的结果
            #         list_row_data.append(
            #             [mark_time, mark_project, data_type, b, mark_doctor1, mark_doctor2, '有医生注释', arbitrate_doctor, arbitrate_time,
            #              '数据不可用'])
            print(len(list_row_data))
            for a in range(0, len(list_row_data)):
                for b in range(0, len(list_row_data[a])):
                    sheet2.write(a + 1, b, list_row_data[a][b], set_style_1('Time New Roman', 205,
                                                                            False) if b == 0 or b == 2 or b == 7 else set_style_1(
                        '宋体', 205, False))

            for i in range(0, 10):
                if i == 3 or i == 9:
                    first_col = sheet2.col(i)  # xlwt中是行和列都是从0开始计算的
                    first_col.width = 256 * 23
                else:
                    first_col = sheet2.col(i)  # xlwt中是行和列都是从0开始计算的
                    first_col.width = 256 * 12

            workboot.footer_str = b''
            workboot.header_str = b''
            workboot.save('/media/tx-eva-data/Data4/CE_DATA/CE_三四级文件/数据试标记记录/lobe/%s.xls' % file_name)


def get_anno_data(hospital_name):
    '''
    :param hospital_name:
    :return:  返回的是对应症状的dict 其中key是pid value: 多发 或者 弥漫
    '''
    hospital_all = get_hosp_dict()
    hospital_id = hospital_all[hospital_name]  # 对应标注医院的id
    symptom_dict = {}
    anno_path = "/media/tx-eva-data/NAS/new_addData/tmp1"
    for hosp_id in os.listdir(anno_path):
        if hosp_id == hospital_id:
            hos_path = os.path.join(anno_path, hosp_id)
            for sfile in os.listdir(hos_path):
                for pid in os.listdir(os.path.join(hos_path, sfile)):
                    symptom_dict[pid] = sfile

    return symptom_dict


# 根据不同的项目去获取对应下面的标注数据库的总量 在根据每条记录所需要的标记量在返回 相应的数量的pid
def get_pid(mark_number, mark_project, hospital_name):
    '''
    TODO 找到对应的医院获取pid
    :param hospital_id:
    :param number: 需要的PId数量
    :return
    '''
    hospital_all = get_hosp_dict()
    hospital_id = hospital_all[hospital_name]
    list_pid = []  # 保存每一个批次里面的标注的pid
    src_path = "/media/tx-eva-data/Data4/CE_DATA/标注数据库/lobe/dcm"
    for file in os.listdir(src_path):
        if hospital_id in file:
            list_pid.append(file)

    return list_pid


def get_baseData(hosp_name):
    path = "/media/tx-eva-data/NAS/基础数据库/" + hosp_name
    pici_dict = {}
    for file in os.listdir(path):
        list_pid = []
        for sfile in os.listdir(os.path.join(path, file)):
            list_pid.append(sfile)
        pici_dict[file[:10]] = list_pid

    return pici_dict


def set_style_1(name, height, bold=False):
    style = xlwt.XFStyle()
    font = xlwt.Font()
    align = xlwt.Alignment()
    # 设置单元格对齐方式
    alignment = xlwt.Alignment()
    borders = xlwt.Borders()
    borders.left = xlwt.Borders.THIN
    borders.right = xlwt.Borders.THIN
    borders.top = xlwt.Borders.THIN
    borders.bottom = xlwt.Borders.THIN
    borders.left_colour = 0x40
    borders.right_colour = 0x40
    borders.top_colour = 0x40
    borders.bottom_colour = 0x40
    font.name = name
    font.bold = bold
    font.color_index = 4
    font.height = height
    style.font = font
    style.alignment = align
    style.borders = borders
    return style


if __name__ == '__main__':
    list_old_pid = []
    split_excel(list_old_pid)
