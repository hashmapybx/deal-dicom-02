# -*- coding: utf-8 -*-
"""
Create Time: 2019/8/30 下午6:53
Author: ybx
"""

import pydicom,os,shutil
'''
筛出纵膈窗
'''
path = '/media/tx-eva-data/Data3/bejiingdaxueshenzhenfushuyiyuan/test_data/bdsz_test_data_save/CT/'
zongge_path = '/media/tx-eva-data/Data3/bejiingdaxueshenzhenfushuyiyuan/test_data/bdsz_test_data_save/zongge'
for folder in os.listdir(path):
    folder_path = os.path.join(path,folder)
    folderName = folder_path.split('/')[-1]
    print(folderName)
    for folder_name in os.listdir(folder_path):
        folder_name_path = os.path.join(folder_path,folder_name)
        pid = folder_name_path.split('/')[-1]
        print(pid)
        for series_path in os.listdir(folder_name_path):
            series_folder_name_path = os.path.join(folder_name_path, series_path)
            seriesName = folder_name_path.split('/')[-1]
            try:
                for dcm_file in os.listdir(series_folder_name_path):

                    dcm_file_path = os.path.join(series_folder_name_path, dcm_file)
                    print(dcm_file_path)
                    ds = pydicom.read_file(dcm_file_path, stop_before_pixels=True, force=True)
                    center = ds.WindowCenter
                    width = ds.WindowWidth
                    if isinstance(center, pydicom.multival.MultiValue):
                        center = center[0]
                    if isinstance(width, list):
                        width = width[0]
                    out_path = os.path.join(zongge_path, folderName)
                    # save_path = os.path.join(out_path, seriesName)
                    if not os.path.exists(out_path):
                        os.makedirs(out_path)
                    if center > 0:
                        print(center)
                        shutil.move(folder_name_path, out_path)
                    break
            except:
                pass