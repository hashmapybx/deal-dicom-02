# -*- coding: utf-8 -*-
"""
Create Time: 2019/9/24 下午6:51
Author: ybx
"""
import os
import shutil
import pandas as pd
root_path = "/media/tx-eva-data/Data4/厦门/all_save"
xls_path = "/media/tx-eva-data/Data2/Xray/XiaMen/2019_09_24_XiaMen_xray/normal.xls"
out_path = "/media/tx-eva-data/Data4/厦门/normal"
xls_info = pd.read_excel(xls_path,decoding = 'utf-8')
pid = xls_info.PATIENT_ID
id_list = []
count = 0
for index,value in enumerate(pid):
    id_list.append(str(value))
for p_folder in os.listdir(root_path):
    p_folder_path = os.path.join(root_path,p_folder)
    if p_folder in id_list:
        shutil.move(p_folder_path,out_path)
        count += 1
print(count)