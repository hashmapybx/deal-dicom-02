# -*- coding: utf-8 -*-
"""
Create Time: 2019/9/17 下午6:12
Author: ybx
"""
import os
import pydicom
src_path = "/media/tx-eva-data/NAS/基础数据库/华中科技大学同济医学院附属同济医院/2017_07_13_normal"
dec_path = "/media/tx-eva-data/NAS/原始数据库/华中科技大学同济医学院附属同济医院"
for file in os.listdir(src_path):

        for tfile in os.listdir(os.path.join(src_path, file)):
            dcm_path = os.path.join(os.path.join(src_path, file), tfile)
            pid = dcm_path.split('/')[-2].split('-')[0]
            new_path = '/'.join(dcm_path.split('/')[6:-2])

            info = pydicom.read_file(dcm_path, force=True)
            pid = info.PatientID
            studyInstanceUID = info.StudyInstanceUID
            seriesInstanceUID = info.SeriesInstanceUID
            sopInstanceUID = info.SOPInstanceUID
            out_path = os.path.join(dec_path, new_path, pid)
            new_name = os.path.join(studyInstanceUID, seriesInstanceUID)
            save_path = os.path.join(out_path, new_name)
            if not os.path.exists(save_path):
                os.makedirs(save_path)
            info.save_as(os.path.join(save_path, sopInstanceUID + '.dcm'))
            print('finished')