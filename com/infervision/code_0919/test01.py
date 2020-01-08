# -*- coding: utf-8 -*-
"""
Create Time: 2019/9/19 上午10:07
Author: ybx
"""

import os
src_path = "/media/tx-eva-data/Data1/tmp/2019_09_16_fracture_KLMY_test/label/CT/2019-09-18_DATA-312"
list_pid = []
for file in os.listdir(src_path):
    if file == "source.csv":
        continue
    list_pid.append(file)

with open('/home/tx-eva-data/PycharmProjects/deal-dicom-02/com/infervision/code_0919/pid.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        line  = line.strip()
        if line in list_pid:
            list_pid.remove(line)


for id in list_pid:
    print(id)





