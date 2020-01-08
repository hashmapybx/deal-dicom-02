# -*- coding: utf-8 -*-
"""
Create Time: 2019/11/13 下午4:24
Author: ybx
"""

import os
import xlrd
import shutil
xls_path = '/media/tx-eva-data/CE_DR/标记数据_反馈给模型/正式标记_150.xls'
dcm_path = '/media/tx-eva-data/CE_DR/标注数据库/train_data_2634'
save_path = '/media/tx-eva-data/CE_DR/标记数据_反馈给模型/train_150'
boot = xlrd.open_workbook(xls_path)
sheet = boot.sheets()[0]
# print(sheet.nrows)
list_a = []
for row in range(sheet.nrows):
    list_a.append(sheet.row_values(row)[0])

# list_b = set()
# for file in os.listdir(save_path):
#     list_b.add(file[:-4])
#
# for id in list_a:
#     if id not in list_b:
#         print(id)

# count = 0

for file in os.listdir(dcm_path):
    a_folder = os.path.join(dcm_path, file)
    for sfile in os.listdir(a_folder):
        b_folder = os.path.join(a_folder, sfile)
        for tfile in os.listdir(b_folder):
            new_file = tfile[:-4]
            if new_file in list_a:
                  try:
                    shutil.copy(os.path.join(b_folder, tfile), os.path.join(save_path, tfile))
                  except:
                    pass
#
# print(count)
# for id in list_a:
#     if id not in list_b:
#         print(id)
