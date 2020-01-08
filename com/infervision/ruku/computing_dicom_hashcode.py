# -*- coding: utf-8 -*-
"""
Create Time: 2019/9/17 上午10:09
Author: ybx
"""
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element
import os
from os.path import dirname, abspath
import hashlib
import time
import sys
from multiprocessing import Process, Queue



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
      dcmFilePath = xmlFilePath.replace('label','dicom').replace('xml','dcm')
      dcmFileHash = md5(dcmFilePath)
      write_XML(xmlFilePath,dcmFileHash)
      print(xmlFilePath)


if __name__ == '__main__':

    labelFilePath = '/media/tx-eva-data/Data1/58server/dcm/2018.03.31_ct_ShangHaiTongJiYiYuan_detection/tmp3/tmp/A'
    startTime = time.time()
    for folders_path,folders,files in os.walk(labelFilePath):
        for anno_folder in folders:
            if anno_folder == "label":
                anno_folder_path = os.path.join(folders_path, anno_folder)
                traverse_directory(anno_folder_path)
    endTime = time.time() - startTime
    print(endTime)









