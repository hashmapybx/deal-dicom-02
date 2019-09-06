# -*- coding: utf-8 -*-
"""
Create Time: 2019/9/3 上午10:51
Author: ybx
"""

import pandas as pd

import os
import hashlib


def get_list():
    '''
    获取记录人和审核人那两行数据
    :return:
    '''
    a_path = "/media/tx-eva-data/Data1/dailyFile/数据清洗记录copy.xlsx"
    #
    df1 = pd.read_excel(a_path)
    # # print(list(df1.columns))
    # print(df1)
    a_list = list(df1.loc[47].values)[1:]
    b_list = list(df1.loc[48].values)[1:]
    print(a_list)
    print(b_list)
    return a_list, b_list
# print(a_list[-3])
# print(list(df.loc[47].values))

def delete_row(src_path):
    '''
    删除数据表中多余的列名称
    :param src_path:
    :param a_list:
    :param b_list:
    :return:
    '''
    for file in os.listdir(src_path):
        xls_path = os.path.join(src_path, file)
        # print(xls_path)
        df = pd.read_csv(xls_path, '\t', encoding='utf-8')
        # df = df.rename(columns={"日期.1":'日期'})

        # df2 = pd.DataFrame([[], [], [], [], []])
        # date_time = xls_path.split('/')[-1][:10]
        # a_list[-1] = date_time
        # b_list[-1] = date_time
        for index, row in df.iterrows():
            # print(list(row))
            if '数据所属医院' in list(row):
                df = df.drop([index], axis=0, inplace=False)
                # df = df.append(df2)
                # df.loc[20] = a_list
                # df.loc[21] = b_list
                df.to_csv(xls_path, sep='\t', index=False, encoding='utf-8')
            else:
                # df = df.append(df2)
                # df.loc[20] = a_list
                # df.loc[21] = b_list
                df.to_csv(xls_path, sep='\t', index=False, encoding='utf-8')


def delete_repeat_date(src_path):
    for file in os.listdir(src_path):
        xls_path = os.path.join(src_path, file)
        # print(xls_path)
        df = pd.read_csv(xls_path, '\t', encoding='utf-8')
        # df.fillna('aaaaa')
        # print(df)
        list=[]
        for index, row in df.iterrows():
                if len(str(row['数据所属医院'])) != 0 and len(str(row['数据清洗日期'])) != 0:
                    flag = str(row['数据所属医院']) +'-'+ str(row['数据清洗日期'])
                    if flag not in list:
                        list.append(flag)
                    else:
                        print(row['数据所属医院'], row['数据清洗日期'])
                        #删除对应的行
                        df = df.drop([index], axis=0, inplace=False)

                        df.to_csv(xls_path, sep='\t', index=False, encoding='utf-8')




def add_report_people(src_path, a_list, b_list):
    '''
    在xsl文件的末尾增加记录人和审核人
    :param src_path:
    :param a_list:
    :param b_list:
    :return:
    '''
    for file in os.listdir(src_path):
        xls_path = os.path.join(src_path, file)
        # print(xls_path)
        df = pd.read_csv(xls_path, '\t', encoding='utf-8')
        df2 = pd.DataFrame([[], [], [], [], []])
        date_time = xls_path.split('/')[-1][:10]
        a_list[-1] = date_time
        b_list[-1] = date_time
        df = df.append(df2)
        df.loc[20] = a_list
        df.loc[21] = b_list
        df.to_csv(xls_path, sep='\t', index=False, encoding='utf-8')


if __name__ == '__main__':

    src_path = "/media/tx-eva-data/Data1/dailyFile/清洗表/split"
    # delete_repeat_date(src_path)
    a_list, b_list = get_list()
    # delete_row(src_path)
    add_report_people(src_path,a_list, b_list)



