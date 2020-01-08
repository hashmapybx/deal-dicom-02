# -*- coding: utf-8 -*-
"""
Create Time: 2019/10/31 上午11:49
Author: ybx
"""
import xml.etree.cElementTree as ET
import os
path = '/media/tx-eva-data/Data1/dailyFile/anno'
for file in  os.listdir(path):
    f_folder = os.path.join(path, file)
    for sfile in os.listdir(f_folder):
        xmL_path = os.path.join(f_folder, sfile)
        tree = ET.parse(xmL_path)
        root = tree.getroot()
        objects = root.findall('object')
        for obj in objects:
            if str(obj.find('L_Diameter_mm').text) == 'Na' or  str(obj.find('S_Diameter_mm').text) == 'Na':
                obj.find('L_Diameter_mm').text = 'none'
                obj.find('S_Diameter_mm').text = 'none'
        tree.write(xmL_path, encoding='utf8', xml_declaration=True)


