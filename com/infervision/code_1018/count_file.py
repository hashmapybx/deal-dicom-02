# -*- coding: utf-8 -*-
"""
Create Time: 2019/10/24 下午3:57
Author: ybx
"""
import os
import xlrd
from collections import Counter

path = "/media/tx-eva-data/Data3/dcm"
excel_path = '/home/tx-eva-data/Desktop/all_info.xls'

table = xlrd.open_workbook(excel_path)
list_pid = []
sheet1 = table.sheets()[0]
rows = sheet1.nrows

for row in range(0, rows):
    if row == 0:
        # 跳过表的表头
        continue
    else:
        list_pid.append(sheet1.row_values(row)[0])  # pid

b = dict(Counter(list_pid))
print ([key for key,value in b.items()if value > 1])



list_a = []

for file in os.listdir(path):
    list_a.append(file)

print(len(set(list_a)))

# for id in list_pid:
#     if id not in list_a:
#         print(id)
