# -*- coding: utf-8 -*-
"""
Create Time: 2019/11/7 下午2:00
Author: ybx
"""


import os
import xlrd

path = '/media/tx-eva-data/CE_DR/CE_DR_error_data/8-9_info.xlsx'

boot = xlrd.open_workbook(path)
sheet = boot.sheets()[0]
rows = sheet.nrows
print(rows)
list_info = {}

for row in range(rows):
    list_info[sheet.row_values(row)[0]] = sheet.row_values(row)[1]

path_1= '/media/tx-eva-data/CE_DR/train/data_2634/基础数据库/中国人民解放军陆军军医大学第一附属医院/error'
fout = open('/media/tx-eva-data/CE_DR/train/data_2634/基础数据库/中国人民解放军陆军军医大学第一附属医院/' +'error_pid.txt' , 'a+')
count = 0
for file in os.listdir(path_1):
    if file[:-4] in list_info.keys():
        fout.write( file[:-4] + '|' + list_info[file[:-4]]+'\n')
        count += 1

fout.close()
print(count)

