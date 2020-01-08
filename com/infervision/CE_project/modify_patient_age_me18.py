# -*- coding: utf-8 -*-
"""
Create Time: 2019/10/31 下午2:55
Author: ybx
"""

import os
import pydicom
path = '/media/tx-eva-data/Data4/CE_DATA/基础数据库/Vall_dHebron_University_Hospital/modify_age'
save_path = '/media/tx-eva-data/Data4/CE_DATA/基础数据库/Vall_dHebron_University_Hospital/modified_age'
for dirpath, dirnames, filenames in os.walk(path):
    for filename in filenames:
        dcm_path = os.path.join(dirpath, filename)
        instance_number = os.path.split(dcm_path)[-1]
        file_a = os.path.split(dcm_path)[0].replace(path, '')
        info = pydicom.read_file(dcm_path)
        # birthday = int(info.PatientBirthDate)
        age = int(str(info.PatientAge)[1:-1])
        studyDate = int(str(info.StudyDate))
        info.PatientAge = '018Y'
        info.PatientBirthDate = str(studyDate - 18*10000)
        # print('出生日期: %d, 年龄: %d' % (birthday, age))

        new_path = save_path + file_a
        # print(new_path)
        if not os.path.exists(new_path):
            os.makedirs(new_path)
        # print(os.path.join(new_path, instance_number))
        info.save_as(os.path.join(new_path, instance_number))
