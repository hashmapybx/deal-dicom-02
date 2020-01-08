# -*- coding: utf-8 -*-
"""
Create Time: 2019/11/5 下午4:42
Author: ybx
"""

import xlrd
import os
import pydicom
from collections import Counter
# path = '/home/tx-eva-data/Downloads/sctest_info.xls'
# boot = xlrd.open_workbook(path)
# sheet = boot.sheets()[0]
# rows = sheet.nrows
#
list_pid = []
# for row in range(0, rows):
#     if row == 0:
#         continue
#     list_pid.append(sheet.row_values(row)[4])

path = '/media/tx-eva-data/CE_DR/test/China_internal_data_591/data'
for dcm in os.listdir(path):
    # dcm_path = os.path.join(path, dcm)
    # info = pydicom.read_file(dcm_path, force=True, stop_before_pixels=True)
    if '-' in dcm:
        list_pid.append(dcm[:-4].split('-')[0])
    else:
        list_pid.append(dcm[:-4])
# print(list_pid)
path = '/media/tx-eva-data/CE_DR/test/China_internal_data_591/标记数据库'
list_a = []
for file in os.listdir(path):
    hosp_path = os.path.join(path, file)
    for sfile in os.listdir(hosp_path):
        dcm_path = os.path.join(hosp_path, sfile)
        for tfile in os.listdir(dcm_path):
            list_a.append(tfile.split('_')[1])

#
for pid in list_pid:
    if pid not in list_a:
        print(pid)

#
# Counter(list_pid)
a = dict(Counter(list_pid))
# print(len(set(list_pid)))
# print(len(list_a))
print([key for key, value in a.items() if value > 1])
