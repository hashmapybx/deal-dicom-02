# -*- coding: utf-8 -*-
"""
Create Time: 2019/10/15 上午11:14
Author: ybx
"""

import os
import shutil

anno_path = '/media/tx-eva-data/NAS/new_addData/备份_不要删/segmentation/seg_xml'
save_path = '/media/tx-eva-data/NAS/标注数据库/交付数据/segmentation/tmp_anno'
list_a = []
with open('/home/tx-eva-data/PycharmProjects/deal-dicom-02/com/infervision/code_1014/outer_pid_seg.txt', 'r', encoding='utf-8') as fin:
    for h_id in fin.readlines():
        h_id = h_id.strip()
        list_a.append(h_id[9:h_id.rfind('T')-1])

print(len(list_a))

for file in os.listdir(anno_path):
    pid = file[9:file.rfind('T')-1]
    if pid in list_a:
        shutil.copytree(os.path.join(anno_path, file), os.path.join(save_path, file))



