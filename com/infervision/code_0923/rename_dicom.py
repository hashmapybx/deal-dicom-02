# -*- coding: utf-8 -*-
"""
Create Time: 2019/9/24 上午11:04
Author: ybx
"""

'''
该脚本使用来在把data-clean 脚本跑完之后在  对于之后的数据还原回 pid + StudyInstanceUID + seriesInstanceUID +sop 的命名方式 
在把数据备份到58上面去 

'''

import os
import pydicom
import shutil
import random

dcm_path = "/media/tx-eva-data/Data3/tx-xray_data/Tongji/tj_cr_menzhen_all/mnt/PACSS"
out_path = "/media/tx-eva-data/Data3/tx-xray_data/Tongji/tj_cr_menzhen_all/mnt/tmp"
# hosp = 'CN411002'



for dirpath, dirname, filenames in os.walk(dcm_path):
    for file in filenames:
        dicom_path = os.path.join(dirpath, file)
        # pid = dicom_path.replace(dcm_path, '').split('/')[1]
        info = pydicom.read_file(dicom_path, force=True)
        try:
            seriesInstanceUID = info.SeriesInstanceUID
        except:
            print(dicom_path)
            seriesInstanceUID = 'NA'
        try:
            sopInstanceUID = info.SOPInstanceUID
        except:
            sopInstanceUID = 'NA'
        # print(pid)
        save_path = os.path.join(out_path, str(seriesInstanceUID))
        if not os.path.exists(save_path):
            os.mkdir(save_path)
        shutil.move(dicom_path, os.path.join(save_path, str(sopInstanceUID) + '.dcm'))
#         info = pydicom.read_file(dicom_path, force=True)
#         # thick = "{0:0<4}".format(str(info.SliceThickness)).replace('.', '')
#         # instancenumber = format(int(info.InstanceNumber), '03d')
#         # print(thick)
#
#         new_name = hosp + '-' + pid + '-'+str(random.randint(000, 999)).zfill(4)
#         # print(new_name)
#         shutil.move(dicom_path, os.path.join(save_path, new_name + '.dcm'))


        # studyInstanceUID = info.StudyInstanceUID
        # seriesInstanceUID = info.SeriesInstanceUID
        # sopInstanceUID = info.SOPInstanceUID
        # new_name = os.path.join(pid, studyInstanceUID, seriesInstanceUID)
        # save_path = os.path.join(out_path, new_name)
        # # print(save_path)
        # if not os.path.exists(save_path):
        #     os.makedirs(save_path)
        # info.save_as(os.path.join(save_path, sopInstanceUID + '.dcm'))
        # print('finished')





