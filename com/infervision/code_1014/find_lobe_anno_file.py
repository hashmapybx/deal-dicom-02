# -*- coding: utf-8 -*-
"""
Create Time: 2019/10/15 上午11:08
Author: ybx
"""
import os
import shutil

anno_path= '/media/tx-eva-data/NAS/标注数据库/交付数据/lobe/test/2018_01_15/anno'
save_path = '/media/tx-eva-data/NAS/标注数据库/交付数据/lobe/tmp_anno'
list_a = []
with open('/home/tx-eva-data/PycharmProjects/deal-dicom-02/com/infervision/code_1014/outer_pid_lobe.txt', 'r', encoding='utf-8') as fin:
    for h_id in fin.readlines():
        list_a.append(h_id.strip())

for file in os.listdir(anno_path):
    if file in list_a:
        shutil.copytree(os.path.join(anno_path, file), os.path.join(save_path, file))




