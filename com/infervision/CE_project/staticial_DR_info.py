# -*- coding: utf-8 -*-
"""
Create Time: 2019/10/30 下午5:21
Author: ybx
"""

import os
path = '/media/tx-eva-data/Data1/pachong/dcm'

# list = ['名称','病例数(按PID)','图象数(按单张dcm)']
list_country = set()
list_pid = []
pid_country = {'BY':[], 'IN':[], 'GE':[], 'RO':[]}
pid = []
for file in os.listdir(path):
    list_pid.append(file)
    pid_folder = os.path.join(path, file)
    for sfile in os.listdir(pid_folder):
        list_country.add(sfile)
        if sfile not in pid_country.keys():
            pid.append(file)
            pid_country[sfile] = pid
        else:
             list_res = pid_country[sfile]
             list_res.append(file)
             pid_country[sfile] = list_res




list_dcm_path = []

for dirpath, dirnames, filenames in os.walk(path):
    for filename in filenames:
        dcm_path = os.path.join(dirpath, filename)
        list_dcm_path.append(dcm_path)


print(len(list_country))
print(len(list_pid))
print(len(list_dcm_path))

print(pid_country)

for key, value in pid_country.items():
    print('country: %s, pid数量是:%d' % (key, len(value)))


dict_country = {}
# count = 0
# for country in list_country:
#     for ppath in list_dcm_path:
#      if country in ppath and iiid in ppath:
#         if country not in dict_country.keys():
#             dict_country[country] = 1
#         else:
#             dict_country[country] = dict_country[country] + 1
# print(dict_country)