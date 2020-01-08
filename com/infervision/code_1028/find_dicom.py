# -*- coding: utf-8 -*-
"""
Create Time: 2019/10/29 下午6:13
Author: ybx
"""

import os
import xlrd
excel_path = '/media/tx-eva-data/Data1/CE_filer/CE测试数据list.xlsx'
table = xlrd.open_workbook(excel_path)
sheet1 = table.sheets()[0]
list_lobe = []
list_detection = []
list_seg = []
print(sheet1.nrows)
rows = sheet1.nrows
for  row in range(0, rows):
    if row == 0:
        continue
    else:
        list_lobe.append(sheet1.row_values(row)[0])
        list_detection.append(sheet1.row_values(row)[1])
        list_seg.append(sheet1.row_values(row)[2])

print(list_detection)
new_list = []
for id in list_detection:
    if str(id)[-2] == '.':
        new_list.append(str(id)[:-2])
    else:
        new_list.append(str(id))
print(new_list)
path = '/media/tx-eva-data/Data4/CE_DATA/原始数据库/XCoop/tmp'
list_a = []
for file in os.listdir(path):
    if '-' in file:
        list_a.append(file.split('-')[0])

count = 0

for id in list_a:
    if id in new_list:
        count += 1

print(count)
