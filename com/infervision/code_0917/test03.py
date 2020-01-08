# -*- coding: utf-8 -*-
"""
Create Time: 2019/9/17 下午2:10
Author: ybx
"""
'''
把基础数据库里面的TMP文件的目录 name保存到文件里面 以便后面数据的追溯
'''
import os

src_path = "/media/tx-eva-data/NAS/基础数据库"
file = open('/home/tx-eva-data/PycharmProjects/deal-dicom-02/com/infervision/code_0917/report.txt', 'a', encoding='utf-8')
for hosp in os.listdir(src_path):
    hosp_path = os.path.join(src_path, hosp)
    for pici in os.listdir(hosp_path):
        if pici == 'TMP':
            tmp_path = os.path.join(hosp_path, pici)
            for symptom in os.listdir(tmp_path):
                sympt_path = os.path.join(tmp_path, symptom)
                for pid in os.listdir(sympt_path):
                    file.write('%s|%s|%s\n' % (hosp, symptom, pid))

file.close()

