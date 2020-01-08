# -*- coding: utf-8 -*-
"""
Create Time: 2019/12/17 下午5:40
Author: ybx
"""

import os
import sys
import boto3
import requests
import json
from com.infervision.s3_service import private_config
import botocore
import configparser
import pymysql
import time

import pandas as pd


def get_coon_tx():
    # 需要穿进去配置文件路径
    path= '/home/tx-eva-data/PycharmProjects/deal-dicom-02/conf/mysql.ini'
    cf = configparser.ConfigParser()
    cf.read(path)
    sections = cf.sections()  # 返回list
    items = cf.items("mysql_tx")
    d_conf = dict(items)
    d_conf['port'] = int(d_conf['port'])
    conn = pymysql.connect(**d_conf)
    return conn


def test_connection(endPointUrl,access_key, secret_key):
    s3 = boto3.resource(service_name='s3', aws_access_key_id=access_key,
                        aws_secret_access_key=secret_key, endpoint_url=endPointUrl,
                        verify=False)

    dcm_bucket = s3.Bucket('dicom')
    label_bucket = s3.Bucket('label')
    return dcm_bucket, label_bucket


def query_mysql_value():
    conn = get_coon_tx()
    cursor = conn.cursor()
    result_list = []
    # sql = "select remote_path from t_dicom_information where date_format(create_date, '%Y-%m-%d %H:%i') = '2019-12-17 16:17'"
    item = "2019-08-30_DATA-149"
    sql = "select B.remote_path from " \
          "(select b.collect_id from t_examine_information as a join t_series_information as b on a.id = b.examine_id where a.accession_number=  ) as A " \
          "join t_dicom_information as B on A.collect_id = B.collect_id" % item


    cursor.execute(sql)
    res_lists = cursor.fetchall()
    for item in res_lists:
        result_list.append(item[0])
    cursor.close()
    return result_list

def post_data(value):
    endPointUrl = private_config.endPointUrl
    access_key = private_config.access_key
    secret_key  = private_config.secret_key
    dcm_bucket, label_bucket = test_connection(endPointUrl, access_key, secret_key)
    out_path = '/media/tx-eva-data/Data4/DR_上线医院_test/data'
    if str(value).endswith('.xml'):
        a_path = os.path.join(out_path, 'label', value.split('/')[-1][:-8])
        if not os.path.exists(a_path):
            os.makedirs(a_path)
        label_bucket.download_file(value, os.path.join(a_path, value.split('/')[-1]))
    else:
        b_path = os.path.join(out_path, 'dicom', value.split('/')[-1][:-8])
        if not os.path.exists(b_path):
            os.makedirs(b_path)
        dcm_bucket.download_file(value, os.path.join(b_path, value.split('/')[-1]))



if __name__ == '__main__':
    start = time.time()
    # lists = query_mysql_value()
    # print(lists)

    df = pd.read_csv('/home/tx-eva-data/Desktop/label.csv')
    xml_lists = list(df['label_path'].values)
    # dicom_lists = list(df['remote_path'].values)

    # for value in xml_lists:
    #     post_data(value)

    list_a = ['1f35815a-e1d1-41c2-a80e-77ec45f67ef4/CS592003-18001066-T100_142.xml']

    for dvalue in list_a:
        post_data(dvalue)

    print('程序消耗的时间:', float(time.time() - start))









