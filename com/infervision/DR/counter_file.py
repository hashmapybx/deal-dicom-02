# -*- coding: utf-8 -*-
"""
Create Time: 2019/11/6 上午10:19
Author: ybx
"""
import os

path  = '/media/tx-eva-data/CE_DR/train/data_2634/标记数据库/广州中山大学附属第一医院'

count = 0
list_a =[]
for dirpath, dirnames, filenames in os.walk(path):
    for filename in filenames:
        dcm_path = os.path.join(dirpath, filename)
        instance_number = os.path.split(dcm_path)[-1]
        print(instance_number)
        count += 1
print(count)






