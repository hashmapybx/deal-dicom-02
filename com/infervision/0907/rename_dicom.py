# -*- coding: utf-8 -*-
"""
Create Time: 2019/9/6 下午5:18
Author: ybx
"""

import os

src_path = "/media/tx-eva-data/NAS/标注数据库/交付数据/lobe/train/2018.01.15/other_anno"
hosp_pid = "CN635001"
for file in os.listdir(src_path):
    for sfile in os.listdir(os.path.join(src_path, file)):
        xml_path = os.path.join(os.path.join(src_path, file), sfile)
        new_name = hosp_pid+sfile[8:]
        print(new_name)
        os.rename(xml_path, os.path.join(os.path.join(src_path, file), new_name))
        # print(sfile)
