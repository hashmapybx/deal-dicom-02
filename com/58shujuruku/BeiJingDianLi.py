# -*- coding: utf-8 -*-
"""
Create Time: 2019/12/31 下午6:08
Author: ybx
"""
import time
import os

path = '/media/tx-eva-data/Data4/DR_上线医院_test/BeiJingDianLi/label'
save_path = '/media/tx-eva-data/Data4/DR_上线医院_test/BeiJingDianLi/tmp'
hosp = 'CNBJDL001'
start = time.time()
for file in os.listdir(path):
    new_name = hosp +'-'+ file[:-4]
    # dcm_path  = os.path.join(path, file)
    out_path = os.path.join(save_path, new_name)
    if not os.path.exists(out_path):
        os.mkdir(out_path)

    os.rename(os.path.join(path, file), os.path.join(out_path, new_name + '.xml'))
print('end time %d ' %(time.time() - start))