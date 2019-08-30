# -*- coding: utf-8 -*-
"""
Create Time: 2019/8/30 下午5:41
Author: ybx
"""
import pandas as pd
import datetime
import re
src_path = "/media/tx-eva-data/NAS/模板_new/tmp/标注/标注记录/数据标注记录_正式标注_分割_V1.1.xlsx"

# from xlrd import open_workbook

sheet = pd.read_excel(src_path,sheet_name=[0,1])
# print(sheet[0]['日期'].to_list())
# date = sheet[0]['日期'].to_list()
print(sheet[0].loc[0:1])

# tmp = 0
# try:
#     # print(len(date))
#     for day in date:
#         df = pd.DataFrame(sheet[0].loc[2,:])
#         df.to_excel()
        # print(day)
#         if re.match('\d\.*', day):
# #             把日期按照周来划分
#             ri = re.match('^\d{4}\.\d{1,2}\.(\d{1,2})', day)
#             ri = ri.group(1)



# except:
#     pass



# def deal_date(src_path):
