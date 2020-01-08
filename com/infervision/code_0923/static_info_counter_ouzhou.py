# -*- coding: utf-8 -*-
"""
Create Time: 2019/10/28 下午6:47
Author: ybx
"""
import xlrd
import os
import xlwt


def methos():
    path = '/home/tx-eva-data/Desktop/all_info.xls'
    table = xlrd.open_workbook(path)
    sheet = table.sheets()[0]
    rows = sheet.nrows
    print(rows)
    list_pid = []
    list_age = []
    list_gender = []
    for row in range(0, rows):
        if row == 0:
            continue
        else:
            list_pid.append(sheet.row_values(row)[0])
            list_gender.append(sheet.row_values(row)[2])
            list_age.append(sheet.row_values(row)[4])

    print(len(list_age))
    print(len(list_gender))
    print(len(list_pid))
    zip_1 = zip(list_pid, list_age)
    zip_2 = zip(list_pid, list_gender)
    dict_1 = dict(zip_1)
    dict_2 = dict(zip_2)

    path1 = '/media/tx-eva-data/Data1/pachong/dcm'

    list_rows = []

    for dirpath, dirnames, filenames in os.walk(path1):
        for filename in filenames:
            dcm_path = os.path.join(dirpath, filename)
            pid = dcm_path.split('/')[6]
            # print(pid) # /media/tx-eva-data/Data1/pachong/dcm/2458/BY/1.2.84
            page = dict_1[pid]
            pgender = dict_2[pid]
            list_rows.append([pid, page, pgender])

    workboot = xlwt.Workbook()
    sheet2 = workboot.add_sheet('sheet1', cell_overwrite_ok=True)
    new_clo = ['PID', 'age', 'gender']  # 新表格的列的title
    for col_name in range(len(new_clo)):
        sheet2.write(0, col_name, new_clo[col_name], set_style_1('宋体', 230, True))

    for a in range(0, len(list_rows)):
            for b in range(0, len(list_rows[a])):
                sheet2.write(a+1, b, list_rows[a][b])

    workboot.save(
        "/media/tx-eva-data/Data1/pachong/info_gender_age.xls")


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

# python

if __name__ == '__main__':
    methos()