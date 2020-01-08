# -*- coding: utf-8 -*-
"""
Create Time: 2019/11/6 下午12:01
Author: ybx
"""
import os
import shutil



def move_dicom_forward(path):
    for file in os.listdir(path):
        s_folder = os.path.join(path, file)
        for dcm in os.listdir(s_folder):
            shutil.move(os.path.join(s_folder, dcm), os.path.join(path, dcm))



def delete_dir(path):
    for file in os.listdir(path):
        f_folder = os.path.join(path, file)
        if os.path.isdir(f_folder):
            os.system(' rm -rf %s' % f_folder)


if __name__ == '__main__':
    path = '/media/tx-eva-data/CE_DR/test/China_internal_data_591/基础数据库/广州中山大学附属第一医院/dcm'
    # move_dicom_forward(path)
    delete_dir(path)

