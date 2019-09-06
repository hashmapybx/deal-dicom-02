# -*- coding: utf-8 -*-
"""
Create Time: 2019/9/3 下午6:53
Author: ybx
"""
import os
import shutil

src_path = "/media/tx-eva-data/Data4/大连中山肺不张/tmp"
base_path ="/media/tx-eva-data/Data4/大连中山肺不张/2019_07_08_pulmonary_atelectasis/_dcm"
list_pid = []
for file in os.listdir(base_path):
    list_pid.append(file)


for file in os.listdir(src_path):
    if file not in list_pid:
        print(file)

