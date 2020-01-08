# -*- coding: utf-8 -*-
"""
Create Time: 2019/12/3 下午7:22
Author: ybx
"""

import os
root_path = "/media/tx-eva-data/Data1/git_repository/tmp/InferDetection_TB"
change_date = "2018-05-03"
for folders_path,folders,files in os.walk(root_path):
    for folder in folders:
        folder_path = os.path.join(folders_path,folder)
        os.system('touch -m -d %s %s' %(change_date,folder_path))
    for t_file in files:
        t_file_path = os.path.join(folders_path,t_file)
        os.system('touch -m -d %s %s' %(change_date,t_file_path))