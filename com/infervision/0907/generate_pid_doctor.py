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


def get_hosp_dict():
    xls_path = '/home/tx-eva-data/PycharmProjects/deal-dicom-02/com/infervision/0907/医院对应编号.xlsx'
    read_word = xlrd.open_workbook(xls_path)
    table = read_word.sheets()[0]
    rows = table.nrows
    print(table.nrows)
    dict_a = {}

    for row in range(rows):
        hosp_name = table.row_values(row)[0]
        hosp_id = table.row_values(row)[1]
        dict_a[hosp_name] = hosp_id
    return dict_a


def split_excel():
    src_path = "/home/tx-eva-data/Downloads/正式标注修改0906/数据标注记录_正式标注_检出_v1.1.xlsx"
    save_path = "/home/tx-eva-data/Downloads/正式标注修改0906/split"
    data = xlrd.open_workbook(src_path)
    sheet1 = data.sheets()[0]
    rows = sheet1.nrows
    print(rows)
    list_audit_doctor = [] # 审核医生名字
    list_audit_result = ['通过','意见不一致需要仲裁'] # 审核意见
    list_arbitrate_doctor = [] # 仲裁医生
    list_arbitrate_result = [] # 仲裁结果
    list_status= ['已标','注烂','肺多发'] # 可用状态
    for row_index in range(rows):
        if row_index == 0:
            # 跳过表格的第0行 列的 title
            continue
        else:
            workboot = xlwt.Workbook()  # 每次写的时候创建一个新的xlwt的对象
            sheet2 = workboot.add_sheet('sheet1', cell_overwrite_ok=True)
            new_clo = ['日期', '标注医生', '数据类型', 'PID', '可用状态', '审核医生', '审核结果', '仲裁医生', '仲裁时间', '仲裁状态'] # 新表格的列的title

            for a in range(len(new_clo)):
                sheet2.write(0, a, new_clo[a], set_style_1('宋体', 205, False)) # 写进表格里面去
            # # 2017.4.26	李凤桐	CT肺-结节检出	训练集	华中科技大学同济医学院附属同济医院	LabelIMG	30	30	0	有结节层面不清晰，已反馈	师婧斐
            mark_time = sheet1.row_values(row_index)[0] #标注时间
            mark_doctor = sheet1.row_values(row_index)[1] # 标注医生
            print(mark_doctor)
            mark_project = sheet1.row_values(row_index)[2] # 标注项目
            data_type = sheet1.row_values(row_index)[3]  # 训练集还是测试集
            hospital_name = sheet1.row_values(row_index)[4]
            marked_number = sheet1.row_values(row_index)[7]  # 标注量
            annotation_number = sheet1.row_values(row_index)[8] # 注释量
            # 根据医院的编号去标注数据库读取对应编号的医院的数据 在分配对应数据量的pid
            # 这里还需要注意的是mark_time 必须是对应的数据批次之内的数据 <= 批次的时间
            file_name = mark_time + '--'+mark_project# 生成的新的excel 命名规定
            pid_list = get_pid(mark_time, mark_project, hospital_name)
            # 在从所有满足条件的pid中挑出对应数据量的pid就好了 但是要记住每一次标注的数据不能重复 所以在返回的list里面每次都要记录去重
            marked_number_list = pid_list[:30]
            list_row_data = []
            for pid_index, pid_value in enumerate(marked_number_list):
                # sheet2.write(pid_index+1, , pid_value, )
                list_row_data.append([mark_time, mark_doctor, data_type, pid_value, '已标注','A', '通过', 'B', '2018-10-10', '仲裁完成'])
            print(len(list_row_data))
            for a in range(0, len(list_row_data)):
                for b in range(0, len(list_row_data[a])):
                    sheet2.write(a +1, b, list_row_data[a][b], set_style_1('宋体', 205, False))
            workboot.save( '/home/tx-eva-data/Downloads/正式标注修改0906/split/%s.xls' % file_name)


def get_pid(mark_time, mark_project, hospital_name):

    '''
    TODO 找到对应的医院获取pid
    :param hospital_id:
    :param number: 需要的PId数量
    :return
    '''
    #TODO 根据传进来的医院名称获取医院编号
    hospital_all = get_hosp_dict()
    hospital_id = hospital_all[hospital_name]
    src_path = "/media/tx-eva-data/NAS/标注数据库/交付数据/detection/train"
    list_pid = []
    new_list = []  # 保存传进来对应的医院的pid
    for version in os.listdir(src_path): # 2.0 2.1
        for sfile in os.listdir(os.path.join(src_path, version)):
            #TODO 根据标注的时间在对应的批次之内获取数据
            if int(str(mark_time).replace('.', '')) < int(str(sfile.replace('_', ''))):
                pici_path = os.path.join(os.path.join(src_path, version), sfile)
                for tfile in os.listdir(pici_path):
                    if tfile == "anno":
                        anno_path = os.path.join(pici_path, tfile)
                        for anno_name in os.listdir(anno_path):
                            # 这里想到一个问题 标注数据库中的dcm 和anno必须是匹配的要不然就比较麻烦了 先写程序匹配一下
                            list_pid.append(anno_name)

    #TODO 获取对应医院的pid数据
    for key in list_pid:
        if hospital_id in key:
            new_list.append(key)


    return new_list # 保存着hosp-pid


#TODO 设置表格样式
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
    split_excel()
    # split_excel()
    # list = get_pid('2017.4.26', 'detection', 'CN635001')
    # print(len(list))
