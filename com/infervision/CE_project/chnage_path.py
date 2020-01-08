# -*- coding: utf-8 -*-
"""
Create Time: 2019/12/11 上午10:35
Author: ybx
"""
import  os

path = '/media/tx-eva-data/DR/fanpian'

for file in os.listdir(path):
    a_folder = os.path.join(path, file)
    for sfile in os.listdir(a_folder):
        if not sfile.startswith('CE021004'):
            new_name = 'CE021004' + '_' + sfile
            # print(new_name)
            print(os.path.join(a_folder, new_name))
            # os.rename(os.path.join(a_folder, sfile), os.path.join(a_folder, new_name))