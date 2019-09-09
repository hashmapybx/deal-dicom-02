# -*- coding: utf-8 -*-
"""
Create Time: 2019/9/6 下午2:59
Author: ybx
"""

'''
产生子excel表格 要求正式标注记录表中的每一条记录 找到对应的医院去随机获取到对应的数据量
把这些数据的pid获取到在新生成的excel里面添加一列把这些记录放进去
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
    src_path = "/media/tx-eva-data/Data1/CFDA_file/数据标注/detection_train.xlsx"
    save_path = "/media/tx-eva-data/Data1/CFDA_file/数据标注/detection/split"
    data = xlrd.open_workbook(src_path)
    sheet1 = data.sheets()[0]
    rows = sheet1.nrows
    print(rows)
    # list_audit_doctor = [] # 审核医生名字
    list_audit_result = ['通过', '意见不一致需要仲裁']  # 审核意见 随机给
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
            new_clo = ['日期', '标注医生', '数据类型', 'PID', '可用状态', '审核医生', '审核结果', '仲裁医生', '仲裁时间', '仲裁状态']  # 新表格的列的title

            for a in range(len(new_clo)):
                sheet2.write(0, a, new_clo[a], set_style_1('宋体', 205, False))  # 写进表格里面去
            # # 2017.4.26	李凤桐	CT肺-结节检出	训练集	华中科技大学同济医学院附属同济医院	LabelIMG	30	30	0	有结节层面不清晰，已反馈	师婧斐
            mark_time = sheet1.row_values(row_index)[0]  # 标注时间
            date = datetime.datetime(*xldate_as_tuple(mark_time, 0))
            mark_time = date.strftime('%Y-%m-%d')
            mark_doctor = sheet1.row_values(row_index)[1]  # 标注医生
            print(mark_doctor)
            mark_project = sheet1.row_values(row_index)[2]  # 标注项目
            data_type = sheet1.row_values(row_index)[3]  # 训练集还是测试集
            hospital_name = sheet1.row_values(row_index)[4]  # 医院
            marked_number = sheet1.row_values(row_index)[8]  # 标注量
            annotation_number = sheet1.row_values(row_index)[9]  # 注释量
            audit_doctor = sheet1.row_values(row_index)[10]
            # mark_flag = sheet1.row_values(row_index)[11]
            arbitrate_doctor = sheet1.row_values(row_index)[12]
            arbitrate_time = sheet1.row_values(row_index)[13]
            date = datetime.datetime(*xldate_as_tuple(arbitrate_time, 0))
            arbitrate_time = date.strftime('%Y-%m-%d')
            # 根据医院的编号去标注数据库读取对应编号的医院的数据 在分配对应数据量的pid
            # 这里还需要注意的是mark_time 必须是对应的数据批次之内的数据 <= 批次的时间
            file_name = mark_time + '--' + mark_project + data_type+mark_doctor  # 生成的新的excel 命名规定
            pid_list = get_pid(mark_time, mark_project, hospital_name)
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

            symptoms = get_anno_data(hospital_name) # 拿到所需注释的症状数据 返回是一个dict key是pid value是多发 弥漫等
            list_aaa = list(symptoms.keys())

            if pid in list_symptom_old:
                if pid in list_aaa:
                    list_aaa.remove(pid)

            if int(annotation_number) > 0:
                list_symptom_new = list_aaa[:int(annotation_number)]
                list_symptom_old = list_symptom_old + list_symptom_new


            list_row_data = []  # 保存添加的每一行数据 在往sheet里面write的时候就可以按行去添加 方便操作
            if annotation_number == 0:
                for pid_index, pid_value in enumerate(marked_number_list_new):
                    # sheet2.write(pid_index+1, , pid_value, )

                    a_res = list_audit_result[random.randint(0, 1)]  # 随机每一行产生的审核结果
                    list_row_data.append([mark_time, mark_doctor, data_type, pid_value, '已标注', audit_doctor, a_res,
                                          '' if a_res == '通过' else arbitrate_doctor,
                                          '' if a_res == '通过' else arbitrate_time, '' if a_res == '通过' else '仲裁完成'])
            else:
                for pid_index, pid_value in enumerate(marked_number_list_new):
                    # sheet2.write(pid_index+1, , pid_value, )

                    a_res = list_audit_result[random.randint(0, 1)]  # 随机每一行产生的审核结果
                    list_row_data.append([mark_time, mark_doctor, data_type, pid_value, '已标注', audit_doctor, a_res,
                                          '' if a_res == '通过' else arbitrate_doctor,
                                          '' if a_res == '通过' else arbitrate_time, '' if a_res == '通过' else '仲裁完成'])
                for a, b in enumerate(list_symptom_new):
                    a_res = list_audit_result[random.randint(0, 1)]  # 随机每一行产生的审核结果
                    list_row_data.append(
                        [mark_time, mark_doctor, data_type, pid_value, symptoms[b], audit_doctor, a_res,
                         '' if a_res == '通过' else arbitrate_doctor,
                         '' if a_res == '通过' else arbitrate_time, '' if a_res == '通过' else '仲裁完成'])

            print(len(list_row_data))
            for a in range(0, len(list_row_data)):
                for b in range(0, len(list_row_data[a])):
                    sheet2.write(a + 1, b, list_row_data[a][b], set_style_1('宋体', 205, False))
            workboot.save('/media/tx-eva-data/Data1/CFDA_file/数据标注/detection/split_train/%s.xls' % file_name)


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
    src_path = "/media/tx-eva-data/NAS/标注数据库/交付数据/detection/train"
    list_pid_a = []  # detection 2.0 第一批的pid
    list_pid_b = []  # detection 2.0 第二批的pid
    list_pid_c = []  # detection 2.1 第一批的pid
    list_pid_d = []  # detection 2.1 第二批pid
    for version in os.listdir(src_path):  # 2.0 2.1
        for sfile in os.listdir(os.path.join(src_path, version)):
            if sfile == '2017_11_16':
                pici_path = os.path.join(os.path.join(src_path, version), sfile)
                for tfile in os.listdir(pici_path):
                    if tfile == "anno":
                        anno_path = os.path.join(pici_path, tfile)
                        for anno_name in os.listdir(anno_path):
                            # 这里想到一个问题 标注数据库中的dcm 和anno必须是匹配的要不然就比较麻烦了 先写程序匹配一下
                            list_pid_a.append(anno_name)
            elif sfile == '2018_01_15':
                pici_path = os.path.join(os.path.join(src_path, version), sfile)
                for tfile in os.listdir(pici_path):
                    if tfile == "anno":
                        anno_path = os.path.join(pici_path, tfile)
                        for anno_name in os.listdir(anno_path):
                            list_pid_b.append(anno_name)
            elif sfile == '2018_07_15':
                pici_path = os.path.join(os.path.join(src_path, version), sfile)
                for tfile in os.listdir(pici_path):
                    if tfile == "anno":
                        anno_path = os.path.join(pici_path, tfile)
                        for anno_name in os.listdir(anno_path):
                            list_pid_c.append(anno_name)
            else:
                pici_path = os.path.join(os.path.join(src_path, version), sfile)
                for tfile in os.listdir(pici_path):
                    if tfile == "anno":
                        anno_path = os.path.join(pici_path, tfile)
                        for anno_name in os.listdir(anno_path):
                            list_pid_d.append(anno_name)

    # print('a: %d' % len(list_pid_a))
    # print( 'b: %d' %len(list_pid_b))
    # print('c: %d'%len(list_pid_c))
    # print('d: %d' % len(list_pid_d))
    return list_pid_a, list_pid_b, list_pid_c, list_pid_d


def get_pid(mark_time, mark_project, hospital_name):
    '''
    TODO 找到对应的医院获取pid
    :param hospital_id:
    :param number: 需要的PId数量
    :return
    '''
    # TODO 根据传进来的医院名称获取医院编号
    hospital_all = get_hosp_dict()
    hospital_id = hospital_all[hospital_name]
    src_path = "/media/tx-eva-data/NAS/标注数据库/交付数据/detection/train"
    list_pid = []  # 保存已久拷贝过的pid
    new_list = []  # 保存传进来对应的医院的pid
    list_a, list_b, list_c, list_d = get_markData()
    for version in os.listdir(src_path):  # 2.0 2.1
        for sfile in os.listdir(os.path.join(src_path, version)):
            # TODO 根据标注的时间在对应的批次之内获取数据 20171116 20180115 20180715 20180815
            if int(str(mark_time).replace('-', '')) <= 20171116:
                # 找对应医院的数据pid
                for key in list_a:
                    if hospital_id in key:
                        new_list.append(key)
                return new_list
            if 20171116 < int(str(mark_time).replace('-', '')) <= 20180115:
                for key in list_b:
                    if hospital_id in key:
                        new_list.append(key)
                return new_list
            if 20180115 < int(str(mark_time).replace('-', '')) <= 20180715:
                for key in list_c:
                    if hospital_id in key:
                        new_list.append(key)
                return new_list
            if 20180715 < int(str(mark_time).replace('-', '')) <= 20180815:
                for key in list_d:
                    if hospital_id in key:
                        new_list.append(key)
                return new_list

    # #TODO 获取对应医院的pid数据
    # for key in list_pid:
    #     if hospital_id in key:
    #         new_list.append(key)


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
