# -*- coding: utf-8 -*-
"""
Create Time: 2019/11/4 下午3:27
Author: ybx
"""

import os
import pydicom
import shutil


dcm_path = "/media/tx-eva-data/yushiyan/基础数据库"
out_path = "/media/tx-eva-data/yushiyan/原始数据库"


for dirpath, dirname, filenames in os.walk(dcm_path):
    for file in filenames:
        dicom_path = os.path.join(dirpath, file)
        # pid = dicom_path.split('/')[-2]
        # print(pid)
        if dicom_path.endswith('.dcm'):

            info = pydicom.read_file(dicom_path, force=True)
            hosp_name = dicom_path.split('/')[5]
            pid = dicom_path.split('/')[-2].split('-')[1]
            studyInstanceUID = info.StudyInstanceUID
            seriesInstanceUID = info.SeriesInstanceUID
            sopInstanceUID = info.SOPInstanceUID
            new_name = os.path.join(pid, studyInstanceUID, seriesInstanceUID)
            save_path = os.path.join(out_path, hosp_name, new_name)
            # print(save_path)
            if not os.path.exists(save_path):
                os.makedirs(save_path)
            info.save_as(os.path.join(save_path, sopInstanceUID + '.dcm'))
            print('finished')







