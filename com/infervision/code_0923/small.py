# -*- coding: utf-8 -*-
"""
Create Time: 2019/12/14 下午5:55
Author: ybx
"""

import os
import shutil
path = '/media/tx-eva-data/Data3/tx-xray_data/Tongji/tj_cr_menzhen_all/mnt/tmp'
save_path ='/media/tx-eva-data/Data3/tx-xray_data/Tongji/tj_cr_menzhen_all/mnt/ruku02/dicom/CE027001/2020-01-06_DATA-1295'

i = 0
for file in os.listdir(path):
    i += 1
    if i == 10000:
        break
    shutil.move(os.path.join(path, file), os.path.join(save_path, file))
