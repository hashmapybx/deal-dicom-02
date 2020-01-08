# -*- coding: utf-8 -*-
"""
Create Time: 2019/11/14 上午10:26
Author: ybx
"""
import os
import xml.etree.cElementTree as ET

path = '/media/tx-eva-data/NAS/标注数据库/肺部计算机辅助诊断软件/lobe/train/2018_08_15/anno'

for dirpath, dirnames, filenames in os.walk(path):
    for filename in filenames:
        xml_path = os.path.join(dirpath, filename)
        if not xml_path.endswith('.xml'):
            print(xml_path)
        # print(xml_path)
        tree = ET.parse(xml_path)
        root = tree.getroot()
        dicom = root.find('path')
        # print(dicom)
        try:
            root.remove(dicom)
            tree.write(xml_path)
        except:
            print(xml_path)
            pass
        # for dd in dicom:
        #     print(dd.text)
        # print(type(dicom))







