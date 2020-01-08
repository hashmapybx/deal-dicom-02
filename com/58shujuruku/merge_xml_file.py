# -*- coding: utf-8 -*-
"""
Create Time: 2019/12/30 下午2:51
Author: ybx
"""

import os
import shutil
path = '/media/tx-eva-data/Data3/58server_dataclean/dcm/2017.08.21_ct_DaLianZhongShan_detection/chenbingxu'
save_path = '/media/tx-eva-data/Data3/58server_dataclean/dcm/2017.08.21_ct_DaLianZhongShan_detection/chenbingxu/tmp'
for file in os.listdir(path):
    if file == 'tmp':
        continue
    a_folder =  os.path.join(path, file)
    for sfile in os.listdir(a_folder):
        s_folder = os.path.join(a_folder, sfile)
        try:
            os.system('mv -f %s %s' % (s_folder, os.path.join(save_path, sfile)))
        except:
            pass