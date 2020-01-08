# -*- coding: utf-8 -*-
"""
Create Time: 2019/9/22 下午4:56
Author: ybx
"""
import os
root_path = "/media/tx-eva-data/NAS/标注数据库/交付数据/lobe/test/2018_01_15/anno"
anno_list = []
anno_dic = {}
for anno_folder in os.listdir(root_path):
    anno_list.append(anno_folder)
for key in anno_list:
    hos_num = key.split("-")[0]
    anno_dic[hos_num] = anno_dic.get(hos_num,0)+1
print(anno_dic)
