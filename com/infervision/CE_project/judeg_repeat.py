# -*- coding: utf-8 -*-
"""
Create Time: 2019/11/4 下午7:45
Author: ybx
"""
import os

list_pid = []
path = '/media/tx-eva-data/Data4/songxiaoyuan/2019_10_31_ShenZhenSanYuan_DR/dcm'
for file in os.listdir(path):
    list_pid.append(file)

path_2 =  '/media/tx-eva-data/Data4/songxiaoyuan/2019_11_01_ShenZhenSanYuan_DR/dcm'

for file in os.listdir(path_2):
    if file not in list_pid:
        print(file)
