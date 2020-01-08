# -*- coding: utf-8 -*-
"""
Create Time: 2019/9/8 下午3:00
Author: ybx
"""
'''
unzip 解压到指定目录 
unzip -d /tmp test.zip
unzip  不支持中文的解压 需要加上编码方式
unzip -O CP936 资料.zip 
'''

import os
src_path = "/media/tx-eva-data/Data3/2019-09-02-德化医院/德化县医院/6/2019-09-08_dehuaxianyiyuan_dr_liuyue"
save_path = "/media/tx-eva-data/Data3/2019-09-02-德化医院/德化县医院/6/2019-09-08_dehuaxianyiyuan_dr_liuyue/dicom"
for file in os.listdir(src_path):
    if file == 'report':
        continue
    else:
        os.system('unzip -d %s %s ' % (save_path, os.path.join(src_path, file)))
