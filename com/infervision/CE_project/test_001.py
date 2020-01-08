# -*- coding: utf-8 -*-
"""
Create Time: 2019/10/30 下午4:10
Author: ybx
"""
# -*- coding: utf-8 -*-
import os
import pydicom

'''
这个代码是根据基础数据库还原原始数据库 其中修改原始数据库的命名方式

'''

root_path = "/media/tx-eva-data/Data4/CE_DATA/基础数据库"
path = "/media/tx-eva-data/Data4/CE_DATA/原始数据库"
for h_folder in os.listdir(root_path):
    h_folder_path = os.path.join(root_path, h_folder)
    for dcm_folder in os.listdir(h_folder_path):
        dcm_folder_path = os.path.join(h_folder_path, dcm_folder)
        if dcm_folder == "dcm":
            for p_folder in os.listdir(dcm_folder_path):
                p_folder_path = os.path.join(dcm_folder_path, p_folder)
                for dcm_file in os.listdir(p_folder_path):
                    dcm_file_path = os.path.join(p_folder_path, dcm_file)
                    info = pydicom.read_file(dcm_file_path, force=True)
                    seriesInstanceUID = info.SeriesInstanceUID
                    studyInstanceUID = info.StudyInstanceUID
                    SOPInstanceUID = info.SOPInstanceUID
                    out_path = os.path.join(path, h_folder, p_folder.split('-')[1], studyInstanceUID, seriesInstanceUID)
                    if not os.path.exists(out_path):
                        os.makedirs(out_path)
                    info.save_as(os.path.join(out_path, SOPInstanceUID + ".dcm"))
