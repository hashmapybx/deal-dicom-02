# -*- coding: utf-8 -*-
"""
Create Time: 2019/12/5 下午5:33
Author: ybx
"""

import pandas as pd

path = '/home/tx-eva-data/Documents/ct.xls'

df  = pd.read_excel(path)
keys = list(df.keys())
list_values = list(df.values)
list_dict = [] # 保存每一行的数据 为dict形式 key是每一列的字段名称  如下所示
# {'patientid': 1290095, 'accessionnumber': 1873512, 'ReportTime': '2019-08-26 13:08:42'}
for row in list_values:
    every_row_data = dict(zip(keys, row))
    list_dict.append(every_row_data)
print(len(list_dict))