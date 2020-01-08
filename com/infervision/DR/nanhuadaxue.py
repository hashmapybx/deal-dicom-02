# -*- coding: utf-8 -*-
"""
Create Time: 2019/11/13 下午5:21
Author: ybx
"""

import os
import xml.etree.cElementTree as ET
import sys

path = '/media/tx-eva-data/Data4/nanhuaDaxue/2019_10_18_NanHuaFuEr_fracture/2019-11-13_DATA-485_test/label/CT/2019-11-11_DATA-485'

count = 0
for dirpath, dirnames, filenames in os.walk(path):
    for file in filenames:
        xml_path = os.path.join(dirpath, file)
        tree = ET.parse(xml_path)
        root = tree.getroot()
        dcm = root.find('dcmfileHash').text
        print(dcm)
        count += 1

print(count)