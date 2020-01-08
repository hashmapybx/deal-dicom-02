# -*- coding: utf-8 -*-
"""
Create Time: 2019/10/16 下午12:15
Author: ybx
"""
import xlrd
import xlwt
import os

def method():
    path = "/media/tx-eva-data/Data4/河南/平煤神马医疗集团总医院测试数据医生报告.XLS"

    boot = xlrd.open_workbook(path)
    table = boot.sheets()[0]
    rows = table.nrows
    dict_a = {}
    workboot = xlwt.Workbook()  # 每次写的时候创建一个新的xlwt的对象
    sheet2 = workboot.add_sheet('sheet1', cell_overwrite_ok=True)
    for row in range(rows):
        if row == 0:
            continue
        dicom_id = table.row_values(row)[0].strip()
        conclusion = table.row_values(row)[7].strip()
        desc = table.row_values(row)[10].strip()
        dict_a[dicom_id] = [conclusion, desc]

    new_clo = ['PATIENT_LOCAL_ID',  'DESCRIPTION', 'IMPRESSION']  # 新表格的列的title
    for a in range(len(new_clo)):
        sheet2.write(0, a, new_clo[a], set_style_1('宋体', 205, True))  # 写进表格里面去
    list_pid = get_pid()

    for index, id in enumerate(list_pid):
        new_id = id[9:id.rfind('T')-1]
        if new_id in dict_a:
            list_info = dict_a[new_id]

            list_info.insert(0, id)
            for a_index, info in enumerate(list_info):
                sheet2.write(index +1 , a_index, info, set_style_1('宋体', 205, True))



    workboot.save('/media/tx-eva-data/Data4/河南/dcm_save/report.xls')

def get_pid():
    path = "/media/tx-eva-data/Data4/河南/dcm_save/CT"
    list_pid = []
    for file in os.listdir(path):
        thick_path = os.path.join(path, file)
        for sfile in os.listdir(thick_path):
            # pid = sfile[9:sfile.rfind('T')-1]
            list_pid.append(sfile)
    return list_pid





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
