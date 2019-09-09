# -*- coding: utf-8 -*-
"""
Create Time: 2019/9/9 下午2:43
Author: ybx
"""
import os
import pydicom


src_path ="/media/tx-eva-data/NAS/基础数据库"
d_path = "/media/tx-eva-data/NAS/原始数据库"

list_hosp = {}
for file in os.listdir(src_path):
    for sfile in os.listdir(os.path.join(src_path, file)):
        if sfile == 'TMP':
            tmp_path = os.path.join(os.path.join(src_path, file), sfile)
            list_hosp[file] = tmp_path


for file in os.listdir(d_path):
    if file == '中国人民解放军总医院_301医院' or file == '中南大学湘雅二医院' or file == '中国人民解放军第202医院' or file == '中国人民解放军第307医院':
        continue
    else:
        if file in list_hosp.keys():
            s_path = list_hosp[file]
            for afile in os.listdir(s_path):
                sympotm_path = os.path.join(s_path, afile)
                for sfile in os.listdir(sympotm_path):
                    pid_path = os.path.join(sympotm_path, sfile)
                    for tfile in os.listdir(pid_path):
                        dcm_path = os.path.join(pid_path, tfile)
                        try:
                            pid_index = dcm_path.split('/')[-2].rfind('-T')
                            pid = dcm_path.split('/')[-2][:pid_index]
                        except:
                            pid = dcm_path.split('/')[-2]
                        new_path = '/'.join(dcm_path.split('/')[6:-2])
                        out_path = os.path.join(os.path.join(d_path, file), new_path, pid)
                        # print(out_path)
                        try:
                            info = pydicom.read_file(dcm_path, force=True)
                            studyInstanceUID = info.StudyInstanceUID
                            seriesInstanceUID = info.SeriesInstanceUID
                            sopInstanceUID = info.SOPInstanceUID
                            new_name = os.path.join(studyInstanceUID, seriesInstanceUID)
                            save_path = os.path.join(out_path, new_name)
                            # print(save_path)
                            if not os.path.exists(save_path):
                                os.makedirs(save_path)
                            info.save_as(os.path.join(save_path, sopInstanceUID + '.dcm'))
                        except:
                            print('dicom path is error %s ' % dcm_path) # 这个直接跳过 跳过错误的路径 最后手动把错误的数据在改一下.
                            pass
