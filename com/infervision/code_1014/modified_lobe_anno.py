# -*- coding: utf-8 -*-
"""
Create Time: 2019/10/15 下午1:36
Author: ybx
"""

import os
import xml.etree.cElementTree as ET
path ='/media/tx-eva-data/NAS/标注数据库/交付数据/lobe/tmp_anno'

for file in os.listdir(path):
    a_path = os.path.join(path, file)
    for xml_file in os.listdir(a_path):
        xml_path = os.path.join(a_path, xml_file)
        # print(xml_path)
        tree = ET.parse(xml_path)
        root = tree.getroot()
        for elem in root.iter('lobe_pos'):
            elem.text = str('')
        tree.write(xml_path)



