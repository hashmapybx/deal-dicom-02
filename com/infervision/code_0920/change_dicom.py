# -*- coding: utf-8 -*-
"""
Create Time: 2019/12/10 下午1:13
Author: ybx
"""

import os
import shutil
path = '/media/tx-eva-data/Shuang WU/TB-test-cases/AnonymizationNepal'
save_path = '/media/tx-eva-data/Shuang WU/TB-test-cases/tmp'
for file in os.listdir(path):
    shutil.move(os.path.join(path, file), os.path.join(save_path, file + '.dcm'))
