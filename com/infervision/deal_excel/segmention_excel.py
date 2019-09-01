# -*- coding: utf-8 -*-
"""
Create Time: 2019/8/30 下午5:41
Author: ybx
"""
import pandas as pd
import datetime
import re
import xlrd
import xlwt
import os



# from xlrd import open_workbook

# print(len(x1.sheet_names))
# for i in range(7):
#     print(i)
# pd.read_excel(src_path, sheet_name=len(x1.sheet_names))

# df_raw=pd.read_excel(content,engine='xlrd')

# print(sheet[0]['日期'].to_list())
# date = list(sheet[0]['日期'].values)
# print(list(sheet[0].loc[1].values))
# for index, day in enumerate(date):
#     print(str(index), day)
# # print(date)
# print(sheet[0].iloc[['2017.6.9'], :])
# print(type(sheet[0].columns))
# print(sheet[0].loc[['2017.6.9',]])
# count = 0
# new_list = []
# for index, day in enumerate(date):
#     if re.match('^\d\.*', str(day)):
#         if day not in new_list:
#             count +=1
#             new_list.append(day)
#             df = pd.DataFrame(columns=sheet[0].columns)
#             df.loc[0] = list(sheet[0].loc[index].values)
#             df.to_csv(save_path+'/'+str(day) + '.xls',mode='a', index=False, encoding='utf-8')
#             count =0
#         else:
#             df1 = pd.read_csv(save_path+'/'+str(day) + '.xls',encoding='utf-8')
#             df1.loc[count+1] = list(sheet[0].loc[index].values)
#             df1.to_csv(save_path+'/'+str(day) + '.xls', mode='a', index=False,encoding='utf-8')

#
#
# print("去重之前的长度:%s" % count)
# print("去重之后的长度是:%s" % len(new_list))

# df = pd.DataFrame(columns=sheet[0].columns)
# for k,v in enumerate(sheet[0]['日期'].values):
#     t = 0
#     if str(v) in new_list:
#         if t >= 1:
#             df1 = pd.DataFrame()
#             df1.loc[t-1] = sheet[0].loc[k]
#             pd.concat([df, df1], ignore_index=True)
#             t += 1
#             df.to_csv(save_path+'/'+str(v) + '.xls',mode='a', index=False, encoding='gbk')
#         df.loc[t] = sheet[0].loc[k]
#         t +=1
#         df.to_csv(save_path+'/'+str(v) + '.xls',mode='a', index=False, encoding='gbk')








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



def get_every_date_excel(src_path, save_path):
    content = xlrd.open_workbook(filename=src_path, encoding_override='gbk')
    x1 = pd.ExcelFile(src_path)
    sheets = pd.read_excel(content, engine='xlrd', sheet_name=None, header=1)
    for key in sheets:
        date = list(sheets[key]['日期'].values)
        # print(list(date))
        count = 0
        new_list = []
        for index, day in enumerate(date):
            if re.match('^\d\.*', str(day)):
                if day not in new_list:
                    count +=1
                    new_list.append(day)
                    df = pd.DataFrame(columns=sheets[key].columns)
                    df.loc[0] = list(sheets[key].loc[index].values)
                    df.to_csv(save_path+'/'+str(day) + '.xls',mode='a', index=False, encoding='utf-8')
                    count =0
                else:
                    df1 = pd.read_csv(save_path+'/'+str(day) + '.xls',encoding='utf-8')
                    df1.loc[count+1] = list(sheets[key].loc[index].values)
                    df1.to_csv(save_path+'/'+str(day) + '.xls', mode='a', index=False,encoding='utf-8')


if __name__ == "__main__":
    src_path = "d:/aa/a/数据标注记录_正式标注_分割_V1.1.xlsx"
    # save_path = '/'.join(src_path.split('/')[:-1]) +'/'+src_path.split('/')[-1].split('_')[2]
    save_path = "d:/aa/a/segment"
    # if not os.path.exists(save_path):
    #     os.makedirs(save_path)

    get_every_date_excel(src_path, save_path)