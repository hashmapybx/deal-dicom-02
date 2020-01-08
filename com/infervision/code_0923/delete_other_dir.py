# -*- coding: utf-8 -*-
"""
Create Time: 2019/12/14 下午4:26
Author: ybx
"""

import os

path = '/media/tx-eva-data/Data3/tx-xray_data/Meinian'
for file in os.listdir(path):
    if file == '@eaDir':
        os.system('rm -rf %s' % (os.path.join(path, file),))
    else:
        a_folder = os.path.join(path, file)
        for sfile in os.listdir(a_folder):
            if sfile == '@eaDir':
                os.system('rm -rf %s' % (os.path.join(a_folder, sfile),))
            else:
                b_folder = os.path.join(a_folder, sfile)
                for tfile in os.listdir(b_folder):
                    if tfile == '@eaDir':
                        os.system('rm -rf %s' % (os.path.join(b_folder, tfile),))
                    else:
                        c_folder = os.path.join(b_folder, tfile)
                        for ffile in os.listdir(c_folder):
                            if ffile == '@eaDir':
                                os.system('rm -rf %s' % (os.path.join(c_folder, ffile),))
                            d_folder = os.path.join(c_folder, ffile)