# -*- coding: utf-8 -*-
"""
Create Time: 2019/12/3 上午10:42
Author: ybx
"""

import os

path = '/media/tx-eva-data/yushiyan/标注数据库/anno/without-AI/Zhu_cfda_120-without-AI'
fout = open('/home/tx-eva-data/PycharmProjects/deal-dicom-02/com/CFDA_yushiyan/anno.txt', 'w+')
for file in os.listdir(path):
    fout.write(str(file) + '\n')

fout.close()