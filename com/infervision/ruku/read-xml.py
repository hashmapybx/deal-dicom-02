# -*- coding: utf-8 -*-
"""
Create Time: 2019/9/6 上午10:24
Author: ybx
"""
from xml.etree import ElementTree as ET
xml_path = "/media/tx-eva-data/Data1/tmp/label/CT/2019.09.05_DATA-228/CS591005-540737-T100/CS591005-540737-T100_033.xml"

tree = ET.parse(xml_path)
root = tree.getroot()
data = root.find('object')
all_data = []
for da in data:
    print(da)