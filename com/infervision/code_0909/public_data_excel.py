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
    xls_path = '/home/tx-eva-data/PycharmProjects/deal-dicom-02/com/infervision/0907/医院对应编号.xlsx'
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

def split_excel():

    '''
    对标注记录的excel表拆分操作
    :return:
    '''
    src_path = "/media/tx-eva-data/Data1/CFDA_file/数据标注/public_data_lobe.xlsx"
    data = xlrd.open_workbook(src_path)
    sheet1 = data.sheets()[0]
    rows = sheet1.nrows
    print(rows)
    # list_audit_doctor = [] # 审核医生名字
    list_audit_result = ['通过', '需要仲裁', '需要仲裁', '需要仲裁', '需要仲裁']  # 二合一的结果是随机给但是要保证需要仲裁的结果尽量多一点
    # list_arbitrate_doctor = [] # 仲裁医生
    # list_arbitrate_result = [] # 仲裁结果
    # list_status= ['已标','注烂','肺多发'] # 可用状态
    marked_number_list_old = []  # 记录已经标注过的pid
    marked_number_list_new = []  # 记录当前最新标注的pid
    list_symptom_old = []  # 已经copy过的注释量的pid
    list_symptom_new = []  # 已经当前需要的注释量的pid
    list_aa = []
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
            mark_time = sheet1.row_values(row_index)[0]  # 标注时间
            date = datetime.datetime(*xldate_as_tuple(mark_time, 0))
            mark_time = date.strftime('%Y-%m-%d')  # 转化时间格式 并且转为str
            mark_doctor1 = sheet1.row_values(row_index)[1]  # 标注医生1
            mark_doctor2 = sheet1.row_values(row_index)[2]  # 标注医生1
            print(mark_doctor1, mark_doctor2)
            mark_project = sheet1.row_values(row_index)[3]  # 标注项目
            data_type = sheet1.row_values(row_index)[4]  # 训练集还是测试集
            hospital_name = sheet1.row_values(row_index)[5]  # 医院
            marked_number = sheet1.row_values(row_index)[9]  # 标注量
            annotation_number = sheet1.row_values(row_index)[10]  # 注释量
            arbitrate_doctor = sheet1.row_values(row_index)[13]
            arbitrate_time = sheet1.row_values(row_index)[14]
            date = datetime.datetime(*xldate_as_tuple(arbitrate_time, 0))
            arbitrate_time = date.strftime('%Y-%m-%d')
            print('仲裁医生 %s' % arbitrate_doctor)
            # 根据医院的编号去标注数据库读取对应编号的医院的数据 在分配对应数据量的pid
            # 这里还需要注意的是mark_time 必须是对应的数据批次之内的数据 <= 批次的时间
            file_name = mark_time + '-' + hospital_name+'-'+mark_project + '-' + data_type + '-' + mark_doctor1 + '-' + mark_doctor2  # 生成的新的excel 命名规定
            pid_list = get_markData()
            print(len(pid_list))
            # 在从所有满足条件的pid中挑出对应数据量的pid就好了 但是要记住每一次标注的数据不能重复 所以在返回的list里面每次都要记录去重
            for pid in marked_number_list_old:
                if pid in pid_list:
                    pid_list.remove(pid)
            # 取出来当前医生的标注量
            marked_number_list_new = pid_list[:int(marked_number)]  # 取到每一个医生的标注量放到list里面
            # 每次新取出来的pid 在用的同时都要加入到old的list里面表示已经用过了下次不能在使用了
            for pid in marked_number_list_new:
                marked_number_list_old.append(pid)



            list_row_data = []  # 保存添加的每一行数据 在往sheet里面write的时候就可以按行去添加 方便操作
            if annotation_number == 0:
                for pid_index, pid_value in enumerate(marked_number_list_new):
                    a_res = list_audit_result[random.randint(0, 4)]  # 随机每一行产生的二合一的结果
                    list_row_data.append([mark_time, mark_project, data_type, pid_value, mark_doctor1, mark_doctor2, a_res,
                                          '' if a_res == '通过' else arbitrate_doctor,
                                          '' if a_res == '通过' else arbitrate_time,
                                          '' if a_res == '通过' else '仲裁完成, 数据可用'])
            # else:
            #     # TODO 表示是有注释量的情况下
            #     for pid_index, pid_value in enumerate(marked_number_list_new):
            #         a_res = list_audit_result[random.randint(0, 4)]  # 随机每一行产生的二合一的结果操作
            #         list_row_data.append([mark_time, mark_project, data_type, pid_value, mark_doctor1, mark_doctor2, a_res,
            #                               '' if a_res == '通过' else arbitrate_doctor,
            #                               '' if a_res == '通过' else arbitrate_time, '' if a_res == '通过' else '仲裁完成'])
            #     for a, b in enumerate(list_symptom_new):
            #         # TODO 这里的情况是针对双肺多发 弥漫的症状的 这些特殊情况下面的需要从审核医生那一列开始是为null的
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
            workboot.save('/media/tx-eva-data/Data1/CFDA_file/数据标注/public_date/split_lobe/%s.xls' % file_name)


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


def get_markData():
    '''
    该方法先是获取到对应项目的标注数据的 这里是detection的train
    :return:
    '''
    src_path = "/media/tx-eva-data/NAS/publicData/lobe/2019_08_14_lobe_test_50"
    list_pid_a = []  # detection test 第一批的pid
    list_pid_b = []  # detection test 第二批的pid
    # list_pid_c = []  # detection 2.1 第一批的pid
    # list_pid_d = []  # detection 2.1 第二批pid

    for tfile in os.listdir(src_path):
        if tfile == "dcm":
            dcm_path = os.path.join(src_path, tfile)
            for dcm_name in os.listdir(dcm_path):
                # 这里想到一个问题 标注数据库中的dcm 和anno必须是匹配的要不然就比较麻烦了 先写程序匹配一下
                list_pid_a.append(dcm_name)
        # else:
        #     pici_path = os.path.join(src_path, pici)
        #     for tfile in os.listdir(pici_path):
        #         if tfile == "anno":
        #             anno_path = os.path.join(pici_path, tfile)
        #             for anno_name in os.listdir(anno_path):
        #                 list_pid_b.append(anno_name)

    # print('a: %d' % len(list_pid_a))
    # print( 'b: %d' %len(list_pid_b))
    # print('c: %d'%len(list_pid_c))
    # print('d: %d' % len(list_pid_d))
    return list_pid_a


def get_pid(mark_time, mark_project, hospital_name):
    '''
    TODO 找到对应的医院获取pid 这个的项目是detection test 里面的数据 这个从获取pid
    :param hospital_id:
    :param number: 需要的PId数量
    :return
    '''
    # TODO 根据传进来的医院名称获取医院编号
    hospital_all = get_hosp_dict()
    hospital_id = hospital_all[hospital_name]
    src_path = "/media/tx-eva-data/NAS/publicData/lobe/2019_08_14_lobe_test_50"
    new_list = []  # 保存传进来对应的医院的pid
    list_a= get_markData()
    for version in os.listdir(src_path):  # 2.0 2.1
            if version == 'dcm':
                for key in list_a:
                    if hospital_id in key:
                        # key = CE027001-286755-T100
                        new_list.append(key)
                return new_list
        # if 20171116 < int(str(mark_time).replace('-', '')) <= 20180115:
        #     for key in list_b:
        #         if hospital_id in key:
        #             new_list.append(key)
        #     return new_list


# TODO 设置表格样式
def set_style_1(name, height, bold=False):
    style = xlwt.XFStyle()
    font = xlwt.Font()
    align = xlwt.Alignment()
    align.horz = 0x02  # 设置水平居中
    align.vert = 0x01  # 设置垂直居中
    font.name = name
    font.bold = bold
    font.color_index = 4
    font.height = height
    style.font = font
    style.alignment = align
    return style


if __name__ == '__main__':
    # get_markData()
    split_excel()
    # split_excel()
    # list = get_pid('2017.4.26', 'detection', 'CN635001')
    # print(len(list))
