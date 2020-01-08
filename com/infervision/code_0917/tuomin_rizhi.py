# -*- coding: utf-8 -*-
"""
Create Time: 2019/12/2 下午6:29
Author: ybx
"""
import os
import csv
import logging
root_path = "/media/tx-eva-data/yushiyan/原始数据库"
for h_folder in os.listdir(root_path):
    h_folder_path = os.path.join(root_path,h_folder)
    try:
        for b_folder in os.listdir(h_folder_path):
            if b_folder == 'dcm':
                b_folder_path = os.path.join(h_folder_path,b_folder)
                desensitization_path = os.path.join(h_folder_path,b_folder + "_desensitization.log")
                date = "[ " + (b_folder[:10]).replace("_","-") + " ]"
                os.system('touch %s' %desensitization_path)
                for folders_path,folders,files in os.walk(b_folder_path):
                    for dcm_file in files:
                        dcm_file_path = os.path.join(folders_path,dcm_file)
                        filepath = dcm_file_path.replace(b_folder_path,"")
                        with open(desensitization_path, 'a+') as b:
                            writer = csv.writer(b)
                            writer.writerow(['%s %s\n%s\n%s\n' %(date,dcm_file,filepath,"Sensitive information has been removed ")])
    except:
        print(h_folder_path)