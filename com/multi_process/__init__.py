# -*- coding: utf-8 -*-
"""
Create Time: 2019/11/15 下午5:54
Author: ybx
"""
import xlrd
import os
import pandas as pd

path = '/media/tx-eva-data/Data4/58server上面的数据统计/CT-data/tmp'
list_all = []
for file in os.listdir(path):
    a_folder = os.path.join(path, file)
    df = pd.read_excel(a_folder)
    list_id=list(df['ID'].values)
    list_all.append(list_id)
print(len(list_all))

list_all_id = []
for a in list_all:
    for id in a:
        list_all_id.append(id)

print('总的id的数量', len(list_all_id))
print('去除重复的id', len(set(list_all_id)))

