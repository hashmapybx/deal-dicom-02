# -*- coding: utf-8 -*-
"""
Create Time: 2019/10/18 下午4:26
Author: ybx
"""
import os
import sys
import shutil
import pydicom
import xlwt

' 统计每个医院的 pid manfacture studyDate'


def method():
    root_path = '/media/tx-eva-data/Data4/CE_DATA/MeiYingCiDaXueYiYuan'
    manufacturer_list = []
    boot = xlwt.Workbook()
    sheet1 = boot.add_sheet('sheet1', cell_overwrite_ok=True)

    new_col = ['pid', 'manufacturer', 'studyDate']

    for i in range(len(new_col)):
        sheet1.write(0, i, new_col[i], set_style_1('宋体', 205, True))

    for dirpath, dirnames, filenames in os.walk(root_path):
        for file in filenames:
            dcm_path = os.path.join(dirpath, file)
            info = pydicom.read_file(dcm_path)
            manufacturer = info.Manufacturer
            study_date = info.StudyDate
            manufacturer_list.append(manufacturer)




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
