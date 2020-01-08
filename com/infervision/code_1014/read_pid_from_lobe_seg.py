# -*- coding: utf-8 -*-
"""
Create Time: 2019/10/16 下午4:26
Author: ybx
"""
import os
import xlrd
import xlwt


def method():

    path_1 = '/media/tx-eva-data/NAS/标注数据库/交付数据/segmentation/test/2018_01_16/dcm'
    # path_2 = '/media/tx-eva-data/NAS/标注数据库/交付数据/segmentation/test/2018_01_16/dcm'
    list_a = []
    workboot = xlwt.Workbook()  # 每次写的时候创建一个新的xlwt的对象
    sheet2 = workboot.add_sheet('sheet1', cell_overwrite_ok=True)
    new_clo = ['PATIENT_LOCAL_ID', 'DESCRIPTION', 'IMPRESSION']  # 新表格的列的title
    for a in range(len(new_clo)):
        sheet2.write(0, a, new_clo[a], set_style_1('宋体', 205, True))  # 写进表格里面去

    for file in os.listdir(path_1):
        list_a.append(file)

    dict_hosp = get_hosp_dict()
    new_dict = {value: key for key, value in dict_hosp.items()}
    list_b= []

    for value in list_a:
        hosp_number = value[:8]
        hosp_name = new_dict[hosp_number]
        list_b.append([hosp_name, value])

    for  index, value in enumerate(list_b):
        sheet2.write(index+1, 0, value[0], set_style_1('宋体', 205, True))
        sheet2.write(index+1, 1, value[1], set_style_1('宋体', 205, True))
    workboot.save('/media/tx-eva-data/NAS/标注数据库/交付数据/segmentation/test/2018_01_16/sge_test_pid_hosp.xls')









def get_hosp_dict():
    '''
    根据36家有协议医院name和编号
    :return: dict_a  返回dict
    '''

    xls_path = '/home/tx-eva-data/PycharmProjects/deal-dicom-02/com/infervision/code_0915/医院对应编号.xlsx'
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
    method()