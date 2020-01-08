# -*- coding: utf-8 -*-
"""
Create Time: 2019/11/12 下午5:57
Author: ybx
"""

'''

二合一的操作, 用于把数据分给cjw ll, cbx
用于二合一的数据分发操作

'''

import os
import shutil
import datetime
import math

list_a = ['cbx', 'cjw', 'll']
hosp_name = 'foshan'
curr_time = datetime.datetime.now().strftime('%Y-%m-%d')

anno_path = '/media/tx-eva-data/Data3/佛山市第一人民医院/dcm_save/CT/tmp/anno'
dcm_path = '/media/tx-eva-data/Data3/佛山市第一人民医院/dcm_save/CT/tmp/dcm'
save_path = '/media/tx-eva-data/Data3/佛山市第一人民医院/dcm_save/CT/tmp/tmp'

def assgin_anno():
    list_anno = {}
    for file in os.listdir(anno_path):
        if file not in list_anno:
            list_anno[file] = os.path.join(anno_path, file)

    number = math.ceil(len(list_anno.keys()) / 3)

    # print(number)
    # print(list_anno)
    count = 0
    for i in range(0, 3):
        for key in list(list_anno.keys())[i * number: (i + 1) * number]:
            new_dir = curr_time + '_' + list_a[i] + '_' + hosp_name
            out_path = os.path.join(save_path, new_dir, 'anno')
            if not os.path.exists(out_path):
                os.makedirs(out_path)
            count += 1
            shutil.move(list_anno[key], os.path.join(out_path, key))

    print(count)

def assgin_dcm():
    count = 0
    list_xml= {}
    for file in os.listdir(save_path):
        a_folder = os.path.join(save_path, file)
        for sfile in os.listdir(a_folder):
            b_folder = os.path.join(a_folder, sfile)
            if b_folder.split('/')[-2] not in list_xml:
                list_xml[b_folder.split('/')[-2]] = b_folder

    list_dcm = {}
    for file in os.listdir(dcm_path):
        if file not in list_dcm:
            list_dcm[file] = os.path.join(dcm_path, file)

    for key, value in list_xml.items():
        new_path = value.replace('anno', 'dcm')
        for file in os.listdir(value):
            if file in list_dcm:
                out_path = new_path
                if not os.path.exists(out_path):
                    os.makedirs(out_path)
                shutil.move(list_dcm[file], os.path.join(out_path, file))

if __name__ == '__main__':
    assgin_dcm()