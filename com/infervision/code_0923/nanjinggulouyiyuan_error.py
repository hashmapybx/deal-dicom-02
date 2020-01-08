# -*- coding: utf-8 -*-
"""
Create Time: 2019/12/3 下午3:18
Author: ybx
"""
import os
path = '/media/tx-eva-data/Data3/DATA-159/20190820_ct_lung_delete/20190820_厦门弘爱医院_299/dcm'



list_a = []
path_1 = '/media/tx-eva-data/Data3/DATA-159/20190820_ct_lung_delete/20190820_厦门弘爱医院_299/anno'
for file in os.listdir(path_1):
    list_a.append(file)

for file in os.listdir(path):
    a_folder = os.path.join(path, file)
    for sfile in os.listdir(a_folder):
        if sfile not in list_a:
            print(sfile)


