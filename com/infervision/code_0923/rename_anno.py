# -*- coding: utf-8 -*-
"""
Create Time: 2019/11/29 上午11:27
Author: ybx
"""

import os
import shutil
path ='/media/tx-eva-data/Data3/DATA-159/20190820_ct_lung_delete/CT_Lung_save/anno'
for file in os.listdir(path):
    xml_path = os.path.join(path, file)
    new_name = xml_path[:-8]
    out_path = os.path.join(path, new_name)
    if not os.path.exists(out_path):
        os.makedirs(out_path)
    shutil.move(xml_path, out_path)

