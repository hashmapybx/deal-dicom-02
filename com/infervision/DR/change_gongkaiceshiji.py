# -*- coding: utf-8 -*-
"""
Create Time: 2019/11/6 下午7:18
Author: ybx
"""
import os
path = '/media/tx-eva-data/CE_DR/train/data_2634/标记数据库/中国人民解放军陆军军医大学第一附属医院/anno'
dcm_path = '/media/tx-eva-data/CE_DR/train/data_2634/标记数据库/中国人民解放军陆军军医大学第一附属医院/dcm'

list_a = []
for file in os.listdir(path):
    list_a.append(file[:-4])


list_b= []
for file in os.listdir(dcm_path):
    list_b.append(file[:-4])
count = 0
for id in list_a:
    if id  in list_b:
        print(id)
        count += 1

print(count)
