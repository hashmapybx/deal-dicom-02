# -*- coding: utf-8 -*-
"""
Create Time: 2019/10/11 下午12:49
Author: ybx
"""
import os
import shutil
a_path = "/home/tx-eva-data/Downloads/统计医院及数量5mm/segmentation/5mm/train"
b_path = "/home/tx-eva-data/Downloads/统计医院及数量5mm/detection/5mm/train/has1mm_5mm"
save_path ="/home/tx-eva-data/Downloads/统计医院及数量5mm/segmentation/5mm/tmp"
list_a = []
fout = open('a.txt', 'a')
for file in os.listdir(b_path):
    hosp_path = os.path.join(b_path, file)
    for sfile in os.listdir(hosp_path):
        for tfile in os.listdir(os.path.join(hosp_path, sfile)):
            list_a.append(tfile)
print(len(list_a))
count = 0
for file in os.listdir(a_path):
    hosp_path = os.path.join(a_path, file)
    for sfile in os.listdir(hosp_path):
        if sfile not in list_a:
            print(os.path.join(hosp_path, sfile))
            count += 1
            shutil.move(os.path.join(hosp_path, sfile), os.path.join(save_path, sfile))
fout.close()
print(count)