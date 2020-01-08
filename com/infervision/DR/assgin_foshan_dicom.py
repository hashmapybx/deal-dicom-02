# -*- coding: utf-8 -*-
"""
Create Time: 2019/11/6 上午10:49
Author: ybx
"""

import os
import shutil
label_path = '/media/tx-eva-data/CE_DR/train/data_2634/new_change_anno'
dcm_path = '/media/tx-eva-data/CE_DR/train/data_2634/标记数据库/清华大学医院/dcm'
save_path = '/media/tx-eva-data/CE_DR/train/data_2634/标记数据库/清华大学医院/anno'
list_a = []
for file in os.listdir(dcm_path):
    list_a.append(file[9:-4])


# print(list_a)


for sfile in os.listdir(label_path):
    if sfile[:-4] in list_a:
        shutil.move(os.path.join(label_path, sfile), os.path.join(save_path, sfile))
        # print(sfile)




