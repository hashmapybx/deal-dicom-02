# -*- coding: utf-8 -*-
"""
Create Time: 2019/9/24 下午4:04
Author: ybx
"""
import os
import pydicom
root_path = "/media/tx-eva-data/Data2/Xray/XiaMen/risimage/Shortterm3"
for folders_path, folders, files in os.walk(root_path):
    for dcm_file in files:
        dcm_file_path = os.path.join(folders_path, dcm_file)
        info = pydicom.read_file(dcm_file_path,force=True)
        PatientID = info.PatientID
        SOPInstanceUID = info.SOPInstanceUID
        out_path = root_path+"_save/" + PatientID
        if not os.path.exists(out_path):
            os.makedirs(out_path)
            os.rename(dcm_file_path,os.path.join(out_path, SOPInstanceUID+".dcm"))


