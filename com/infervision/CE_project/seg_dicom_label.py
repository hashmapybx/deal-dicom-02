# -*- coding: utf-8 -*-
"""
Create Time: 2019/11/1 下午7:22
Author: ybx
"""
import os
path = '/media/tx-eva-data/NAS/标注数据库/交付数据/segmentation/test/2018_01_16/dcm'
xml_path = '/media/tx-eva-data/NAS/标注数据库/交付数据/segmentation/test/2018_01_16/xml_label'
list_pid = []
for file in  os.listdir(path):
    list_pid.append(file)


count = 0

for sfile in os.listdir(xml_path):
    if sfile in list_pid:
        count += 1

print(count)

