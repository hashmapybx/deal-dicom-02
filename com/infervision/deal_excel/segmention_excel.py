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


def get_every_date_excel(src_path, save_path):
    # content = xlrd.open_workbook(filename=src_path, encoding_override='utf-8')
    # x1 = pd.ExcelFile(src_path)
    sheets = pd.read_excel(src_path, sheet_name=None, header=3)
    for key in sheets:
        sheets[key] = sheets[key].drop(['Unnamed: 10'], axis=1) # 删除指定的列
        print(sheets[key].columns)
        # print(len(sheets[key].columns))
        date = list(sheets[key]['数据清洗日期'].astype(str).values)
        # print(list(date))
        count = 0
        new_list = {}
        for index, day in enumerate(date):
            if re.match('^\d\-*', str(day)):
                format_day = str(day)[:10]
                print(format_day)
                if format_day not in new_list:
                    count += 1
                    new_list[format_day] = 1
                    df = pd.DataFrame(columns=sheets[key].columns)
                    df.loc[0] = list(sheets[key].loc[index].values)
                    df.to_csv(save_path + '/' + format_day + '.xls', mode='a+', sep='\t',index=False, encoding='utf-8')
                    count = 0
                else:
                    new_list[format_day] = new_list[format_day] + 1
                    df1 = pd.read_csv(save_path + '/' + format_day + '.xls', '\t', encoding='utf-8')
                    # print(df1)
                    # column = list(sheets[key].columns)
                    # print(column)
                    # list1 =list(sheets[key].loc[index].values)
                    # print(list1)
                    # dic = dict(map(lambda x, y: [x, y], column, list1))
                    df1.loc[new_list[format_day] -1] = list(sheets[key].loc[index].values)
                    df1.to_csv(save_path + '/' + format_day + '.xls',  mode='a+',sep='\t', index=False, encoding='utf-8')


if __name__ == "__main__":
    src_path = "/media/tx-eva-data/Data1/dailyFile/数据清洗记录copy.xlsx"
    # save_path = '/'.join(src_path.split('/')[:-1]) +'/'+src_path.split('/')[-1].split('_')[2]
    save_path = "/media/tx-eva-data/Data1/dailyFile/清洗表/split"
    # if not os.path.exists(save_path):
    #     os.makedirs(save_path)

    get_every_date_excel(src_path, save_path)



