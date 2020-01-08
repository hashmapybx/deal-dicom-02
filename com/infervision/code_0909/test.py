# -*- coding: utf-8 -*-
"""
Create Time: 2019/9/10 下午8:24
Author: ybx
"""
import os

src_path = "/media/tx-eva-data/NAS/标注数据库/交付数据/detection/test/2017_11_16/anno"

for file in os.listdir(src_path):
    pid_path = os.path.join(src_path, file)
    for sfile in os.listdir(pid_path):
        xml_end = sfile[-8:]
        new_name = file + xml_end
        os.rename(os.path.join(pid_path, sfile), os.path.join(pid_path, new_name))
