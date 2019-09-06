# -*- coding: utf-8 -*-
"""
Create Time: 2019/9/4 下午12:12
Author: ybx
"""
import os

anno_path = "/media/tx-eva-data/NAS/标注数据库/交付数据/lobe/test/2018.01.15/anno"
time = '2018-01-15'
for file in os.listdir(anno_path):
    os.system('touch -d  %s %s' % (time, os.path.join(anno_path, file)))
    for sfile in os.listdir(os.path.join(anno_path, file)):
        os.system('touch -d  %s %s' % (time, os.path.join(os.path.join(anno_path, file), sfile)))