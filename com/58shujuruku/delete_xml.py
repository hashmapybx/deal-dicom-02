# -*- coding: utf-8 -*-
"""
Create Time: 2020/1/7 下午5:38
Author: ybx
"""

import xml.etree.cElementTree as ET
import os

path = '/media/tx-eva-data/Data1/58server/dcm/2018.03.31_ct_ShangHaiTongJiYiYuan_detection/tmp3/tmp/A/label'

for sfile in os.listdir(path):
    a_folder = os.path.join(path, sfile)
    for ffile in os.listdir(a_folder):
        xml_path = os.path.join(a_folder, ffile)
        tree = ET.parse(xml_path)
        root = tree.getroot()
        a = root.find('dcmfileHash')
        try:
            root.remove(a)
            tree.write(xml_path)
        except:
            pass