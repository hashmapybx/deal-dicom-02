# -*- coding: utf-8 -*-
"""
Create Time: 2019/8/30 下午6:54
Author: ybx
"""
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element
import os
from os.path import dirname, abspath
import hashlib
import time
import sys


def md5(dcmname):
    hash_md5 = hashlib.md5()
    with open(dcmname,'rb')as file:
        for chunk in iter(lambda: file.read(4096),b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest().upper()

def write_XML(xmlname,dcmFileHash):
    tree = ET.parse(xmlname)
    root = tree.getroot()
    dcmHash=Element('dcmfileHash')
    dcmHash.text = dcmFileHash
    root.append(dcmHash)
    tree.write(xmlname)

def traverse_directory(filepath):
  files = os.listdir(filepath)
  for fi in files:
    fi_d = os.path.join(filepath,fi)
    if os.path.isdir(fi_d):
      traverse_directory(fi_d)
    else:
      xmlFilePath = os.path.join(filepath,fi_d)
      dcmFilePath = xmlFilePath.replace('anno','dcm').replace('xml','dcm')
      dcmFileHash = md5(dcmFilePath)
      write_XML(xmlFilePath,dcmFileHash)
      print(xmlFilePath)


if __name__ == '__main__':
    labelFilePath = '/media/tx-eva-22/data4/CT/JC/2019_08_19_CW991005_testData'
    startTime = time.time()
    for folders_path,folders,files in os.walk(labelFilePath):
        for anno_folder in folders:
            if anno_folder == "anno":
                anno_folder_path = os.path.join(folders_path, anno_folder)
                traverse_directory(anno_folder_path)
    endTime = time.time() - startTime
    print(endTime)