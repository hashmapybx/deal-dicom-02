# -*- coding: utf-8 -*-
"""
Create Time: 2019/12/30 下午6:01
Author: ybx

"""

import os
import pydicom
import shutil
import pandas as pd

path_list = []
root_path = "/media/tx-eva-data/Data4/青岛西海岸新区人民薄层数据/薄层1/boceng"


for dirpath, dirname, filenames in os.walk(root_path):
    for filename in filenames:
        dcm_path = os.path.join(dirpath, filename)
        info = pydicom.read_file(dcm_path,force=True,stop_before_pixels=True)
        if "Patient Protocol" == str(info.SeriesDescription):
            path_list.append(dcm_path)
writer = pd.ExcelWriter(root_path+'_protocol.xls',encoding = 'utf-8')
df = pd.DataFrame(data={'PATH':path_list,})
df.to_excel(writer,index=False)
writer.save()


