# -*- coding: utf-8 -*-
"""
Create Time: 2019/9/4 上午11:39
Author: ybx
"""

import os


anno_path = "/media/tx-eva-data/NAS/标注数据库/交付数据/lobe/test/2018.01.15/anno"
dcm_path = "/media/tx-eva-data/NAS/标注数据库/交付数据/lobe/test/2018.01.15/dcm"
list_pid = []
for file in os.listdir(anno_path):
    list_pid.append(file)


list_dcm = []
for file in os.listdir(dcm_path):
    list_dcm.append(file)

for id in list_pid:
    if id not in list_dcm:
        print(id)



