# -*- coding: utf-8 -*-
"""
Create Time: 2020/1/6 下午4:45
Author: ybx
"""

import os
import shutil
path ='/media/tx-eva-data/Data3/58server_dataclean/nas-58-label/wuhantongji'

dict_a = {}
for sfile in  os.listdir(path):
    if sfile == 'tmp':
        continue
    doctor = sfile.split('_')[-1]
    if doctor not in dict_a:
        dict_a[doctor] = [os.path.join(path, sfile), ]
    else:
        aa = list(dict_a[doctor])
        aa.append(os.path.join(path, sfile))
        dict_a[doctor] = aa


for key, value in dict_a.items():
    if len(value) > 1:
        for vv in range(1, len(value)):
            for tfile in os.listdir(value[vv]):
                # print('初始化目录{}, 目的目录: {}'.format(os.path.join(value[vv], tfile), os.path.join(value[0], tfile)))
                try:
                    shutil.move(os.path.join(value[vv], tfile), os.path.join(value[0], tfile))
                except:
                    pass

