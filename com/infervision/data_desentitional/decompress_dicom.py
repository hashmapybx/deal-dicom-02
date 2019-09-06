# -*- coding: utf-8 -*-
"""
Create Time: 2019/9/5 下午6:28
Author: ybx
"""
import os

src_path = "/media/tx-eva-data/Data4/07_29_大连中山/dlzs/nqx_ct_other_body_save"

for dirpath, dirnames, filenames in os.walk(src_path):
    for filename in filenames:
        dcm_path = os.path.join(dirpath, filename)
        os.system('gdcmconv -w %s %s' % (dcm_path, dcm_path))


