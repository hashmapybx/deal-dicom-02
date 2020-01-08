# -*- coding: utf-8 -*-
"""
Create Time: 2019/9/26 下午6:01
Author: ybx
"""
import os
import shutil
import xlrd


path = "/home/tx-eva-data/Downloads/XLSX 工作表.xlsx"
save_path = "/media/tx-eva-data/Data1/train/ruxian/2019_03_18_birads_data/rxmb_save/RXMB/tmp"
dcm_path = "/media/tx-eva-data/Data1/train/ruxian/2019_03_18_birads_data/rxmb_save/RXMB/SIEMENS"

list_pid = []
boot = xlrd.open_workbook(path)
table = boot.sheets()[0]

for row in range(table.nrows):
    list_pid.append(table.row_values(row)[0].strip())
    # print(table.row_values(row)[0])
count = 0
for file in os.listdir(dcm_path):
    if file not in list_pid:
        shutil.move(os.path.join(dcm_path, file), os.path.join(save_path, file))
        print(file)
        count += 1

print(count)

