# -*- coding: utf-8 -*-
"""
Create Time: 2019/11/7 下午2:18
Author: ybx
"""

import os
path = '/media/tx-eva-data/CE_DR/test/China_internal_data_591/基础数据库/中国人民解放军陆军军医大学第一附属医院/error'
hosp = 'CW023007'
for file in os.listdir(path):
    new_name = hosp +'-'+file
    os.rename(os.path.join(path, file), os.path.join(path, new_name))