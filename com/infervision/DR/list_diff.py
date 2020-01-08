# -*- coding: utf-8 -*-
"""
Create Time: 2019/11/6 下午6:26
Author: ybx
"""
import os
path = '/media/tx-eva-data/CE_DR/train/data_2634/标记数据库/中国人民解放军陆军军医大学第一附属医院/renamed_anno'
list_a = []
for file in os.listdir(path):
    list_a.append(file[:-4])


path_1 = '/media/tx-eva-data/CE_DR/train/data_2634/标记数据库/中国人民解放军陆军军医大学第一附属医院/tmp'
list_b = []

for sfile in os.listdir(path_1):
    list_b.append(sfile[:-4])

for id in list_b:
    if id not in list_a:
        print(id)
