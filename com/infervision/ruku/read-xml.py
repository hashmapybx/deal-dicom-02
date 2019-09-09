# -*- coding: utf-8 -*-
"""
Create Time: 2019/9/6 上午10:24
Author: ybx
"""
'''
这个代码是用来解析xml文件的操作的
'''
from xml.etree import ElementTree as ET
xml_path = "/home/tx-eva-data/PycharmProjects/deal-dicom-02/com/infervision/ruku/CE027001-020990-T100_063.xml"

tree = ET.parse(xml_path)
root = tree.getroot()
# print(list(root))
data = root.find('object')
all_data = []
for da in data:
    for aa in da:
        print(aa.text)
