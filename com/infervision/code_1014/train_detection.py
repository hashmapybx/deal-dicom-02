# -*- coding: utf-8 -*-
"""
Create Time: 2019/10/15 下午2:20
Author: ybx
"""


import os

def get_train_file():
    path = "/media/tx-eva-data/NAS/标注数据库/交付数据/detection/train"
    list_a = []
    for file in os.listdir(path):
        revision_path = os.path.join(path, file)
        for sfile in os.listdir(revision_path):
            batch_path = os.path.join(revision_path, sfile)
            for tfile in os.listdir(batch_path):
                if tfile == 'dcm':
                    dcm_dir = os.path.join(batch_path, tfile)

                    for dfile in os.listdir(dcm_dir):
                        pid = dfile[9:dfile.rfind('T') - 1]
                        list_a.append(pid)

    return list_a


def lobe_file():
    list_a = get_train_file()
    seg_path = '/media/tx-eva-data/NAS/标注数据库/交付数据/segmentation/test/2018_01_16/tmp'
    count = 0
    for file in os.listdir(seg_path):
        pid = file[9:file.rfind('T') - 1]
        if pid not in list_a:
            print(file)
            count += 1

    print(count)


lobe_file()