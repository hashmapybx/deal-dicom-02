# -*- coding: utf-8 -*-
"""
Create Time: 2019/10/18 下午6:07
Author: ybx
"""
path = "/media/tx-eva-data/Data4/CE_DATA/Spain/Vall_dHebron_University_Hospital/2019_05_14_Vall_dHebron_test_Data/other"

import os
count = 0
for file in os.listdir(path):
    a_path = os.path.join(path, file)
    for sfile in os.listdir(a_path):
        count = count + len(os.listdir(os.path.join(a_path, sfile)))
print(count)
