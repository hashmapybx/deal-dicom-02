# -*- coding: utf-8 -*-
"""
Create Time: 2019/10/21 上午11:35
Author: ybx
"""
import os
import shutil
anno_path = "/media/tx-eva-data/Data1/tmp/2019_10_22_need_upload_anno/anno"
save_path = "/media/tx-eva-data/Data1/tmp/2019_10_22_need_upload_anno/tmp"
dcm_path = "/media/tx-eva-data/Data4/河南/no_review_merge_bbox/2019_10_21_CS775001_ll/dcm"



list_a = []
for file in os.listdir(anno_path):
    list_a.append(file)

count = 0
for file in os.listdir(dcm_path):
    if file in list_a:
        shutil.move(os.path.join(dcm_path, file), os.path.join(save_path, file))


# print(count)

