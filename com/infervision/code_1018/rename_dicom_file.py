# -*- coding: utf-8 -*-
"""
Create Time: 2019/10/22 上午11:43
Author: ybx
"""
import os

'''
这个脚本用于修改标签之后的数据 进行重命名操作 主要是删除标记之前给添加的尾巴 还原为hosp_pid_Thickness的形式

'''



path ="/media/tx-eva-data/Data3/中山大学附属第七医院/测试数据/zsq_test_data_100_save/2019-10-21_中山大学第七附属_100医院/2019_10_29_CS755001/dicom"
save_path = '/media/tx-eva-data/Data3/中山大学附属第七医院/测试数据/zsq_test_data_100_save/2019-10-21_中山大学第七附属_100医院/2019_10_29_CS755001/tmp'
for file in os.listdir(path):
    new_name = file[:-4]
    a_folder = os.path.join(path, file)
    for sfile in os.listdir(a_folder):
        dcm_path = os.path.join(a_folder, sfile)
        instance_name = sfile[-8:]
        dcm_name = new_name + instance_name
        # print(dcm_name)
        out_path = os.path.join(save_path, new_name)
        if not os.path.exists(out_path):
            os.makedirs(out_path)
        # print(out_path)
        os.rename(dcm_path, os.path.join(out_path, dcm_name))




