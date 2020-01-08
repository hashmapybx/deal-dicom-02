# -*- coding: utf-8 -*-
"""
Create Time: 2019/9/23 下午2:46
Author: ybx
"""

'''
修改CFDA数据库的文件上传时间
'''

import os

src_path = "/media/tx-eva-data/NAS/基础数据库"

for file in os.listdir(src_path):
    time_date = ''
    h_path = os.path.join(src_path, file)
    if len(os.listdir(h_path)) == 2:
        for sfile in os.listdir(h_path):
            if sfile.endswith('.log'):
                continue
            time_date = sfile[:10].replace('_', '-')
        os.system("find %s -name '*' -exec touch -d %s {} \;" %(h_path, time_date))
