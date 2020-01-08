# -*- coding: utf-8 -*-
"""
Create Time: 2019/12/13 下午4:48
Author: ybx
"""

import os
import pandas as pd
import random
path= '/media/tx-eva-data/Data4/58server上面的数据统计/XRAY_data/Original_dicom/shanghai'
save_path= '/media/tx-eva-data/Data4/58server上面的数据统计/CT-data'
list_pid = []
# fout = open(save_path + '/' + 'CT_pid_'+ str(random.randint(000, 999)).zfill(3) +'.txt', 'wd+')
for file in os.listdir(path):
    a_folder = os.path.join(path, file)
    for sfile in os.listdir(a_folder):
        b_foldr = os.path.join(a_folder, sfile)
        for tfile in os.listdir(b_foldr):
            list_pid.append(tfile)




writer = pd.ExcelWriter(save_path + '/' + 'DR_pid_'+ str(random.randint(000, 999)).zfill(3) +'.xls', encoding='unicode_escape')

df = pd.DataFrame(data={'ID': list_pid})
df.to_excel(writer, index=False)
writer.save()






