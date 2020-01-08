# -*- coding: utf-8 -*-
"""
Create Time: 2019/9/24 下午9:58
Author: ybx
"""
import os
import shutil

path = "/home/tx-eva-data/Downloads/CFDA文件_0922/四级文件0922/四级文件0921/30阴性数据筛选记录/阴性数据筛选记录"
for file in os.listdir(path):
    a_path = os.path.join(path, file)
    os.rename(a_path, os.path.join(path, file[:-5]+'.xls'))

