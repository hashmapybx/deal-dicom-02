# -*- coding: utf-8 -*-
"""
Create Time: 2019/9/19 下午5:33
Author: ybx
"""


import os

src_path = "/media/tx-eva-data/Data1/CFDA_file/数据标注/detection/a"
b_path = "/media/tx-eva-data/Data1/CFDA_file/数据标注/detection/split_train_new"

list_a = []
for file in os.listdir(src_path):
    list_a.append(file)

for file in os.listdir(b_path):
    if file not in list_a:
        print(file)

