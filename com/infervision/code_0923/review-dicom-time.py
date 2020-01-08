# -*- coding: utf-8 -*-
"""
Create Time: 2019/9/23 下午9:08
Author: ybx
"""
'''
这个脚本是用来修改基础数据库和原始数据库的文件上传时间
'''




import os
root_path = "/media/tx-eva-data/NAS/基础数据库"
for h_folder in os.listdir(root_path):
    h_folder_path = os.path.join(root_path,h_folder)
    for b_folder in os.listdir(h_folder_path):
        b_folder_path = os.path.join(h_folder_path,b_folder)
        change_date = b_folder.replace("_","-")[:10]
        if os.path.isfile(b_folder_path):
            os.system('touch -m -d %s %s' %(change_date,b_folder_path))
        else:
            for p_folder in os.listdir(b_folder_path):
                p_folder_path = os.path.join(b_folder_path,p_folder)
                for dcm_file in os.listdir(p_folder_path):
                    dcm_file_path = os.path.join(p_folder_path,dcm_file)
                    os.system('touch -m -d %s %s' %(change_date,dcm_file_path))
                os.system('touch -m -d %s %s' %(change_date,p_folder_path))
        os.system('touch -m -d %s %s' %(change_date,b_folder_path))