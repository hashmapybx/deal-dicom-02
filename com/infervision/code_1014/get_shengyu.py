# -*- coding: utf-8 -*-
"""
Create Time: 2019/10/17 下午1:56
Author: ybx
"""

import os
list_a =[]
with open('/home/tx-eva-data/PycharmProjects/deal-dicom-02/com/infervision/code_1014/A.txt', 'r') as fin:
    for file in fin.readlines():
        file = file.strip()
        list_a.append(file)
path = "/media/tx-eva-data/NAS/标注数据库/交付数据/segmentation/test/2018_01_16/anno"

for file in os.listdir(path):
    if (file not in list_a) and ('CE027001' in file):
        print(file)


