# -*- coding: utf-8 -*-
"""
Create Time: 2019/9/22 下午3:51
Author: ybx
"""

import os
import shutil
a_path = "/media/tx-eva-data/NAS/标注数据库/交付数据/lobe/test/2018_01_15/anno"
b_path = "/media/tx-eva-data/NAS/new_addData/备份_不要删/lobe/anno"
save_path = "/media/tx-eva-data/NAS/标注数据库/交付数据/lobe/test/2018_01_15/tmp"
list_a = []

for file in os.listdir(b_path):
    list_a.append(file)

for file in os.listdir(a_path):
    if file in list_a:
        shutil.move(os.path.join(a_path, file), os.path.join(save_path, file))
