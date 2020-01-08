# -*- coding: utf-8 -*-
"""
Create Time: 2020/1/2 下午2:32
Author: ybx
"""

from com.DR_test_download import conn_mysql

import os
import sys
import boto3
import requests
import json
from com.DR_test_download import private_config
import shutil
import random
from multiprocessing import cpu_count, Process, JoinableQueue
import time


def test_connection(endPointUrl, access_key, secret_key):
    s3 = boto3.resource(service_name='s3', aws_access_key_id=access_key,
                        aws_secret_access_key=secret_key, endpoint_url=endPointUrl,
                        verify=False)

    dcm_bucket = s3.Bucket('dicom')
    label_bucket = s3.Bucket('label')
    return dcm_bucket, label_bucket

def download_list_all_dict(version_key, data_dict, dcm_bucket, label_bucket, out_path):
    if isinstance(data_dict, dict):
        folder_keys = data_dict.keys()
        for folder_key in folder_keys:
            if folder_key == "dicoms":
                dicoms_value = data_dict[folder_key]
                target_folder_keys = dicoms_value.keys()
                for target_folder_key in target_folder_keys:
                    target_folder_values = dicoms_value[target_folder_key]
                    dcm_out_path = os.path.join(out_path, version_key, "dicom", target_folder_key)
                    if not os.path.exists(dcm_out_path):
                        os.makedirs(dcm_out_path)
                    for target_folder_value in target_folder_values:
                        dcm_name = target_folder_value.split("/")[1]
                        dcm_bucket.download_file(target_folder_value, os.path.join(dcm_out_path, dcm_name))
            if folder_key == "xmls":
                labels_value = data_dict[folder_key]
                target_folder_keys = labels_value.keys()
                for target_folder_key in target_folder_keys:
                    target_folder_values = labels_value[target_folder_key]
                    label_out_path = os.path.join(out_path, version_key, "label", target_folder_key)
                    if not os.path.exists(label_out_path):
                        os.makedirs(label_out_path)
                    for target_folder_value in target_folder_values:
                        label_name = target_folder_value.split("/")[1]
                        label_bucket.download_file(target_folder_value, os.path.join(label_out_path, label_name))





def queryLabelMysql():
    path = '/home/tx-eva-data/PycharmProjects/deal-dicom-02/conf/mysql.ini'
    conn = conn_mysql.get_coon_tx(path)
    cursor = conn.cursor()
    sql = "select label_path from t_label_information as B join (select label_set_id from t_label_set where label_batch_id = (SELECT batch_id from t_batch_information where batch_name = '%s' )) as A on A.label_set_id = B.Label_set_Id" % '2019-12-31_DATA-1587'
    cursor.execute(sql)
    list_xml= []
    for res in cursor.fetchall():
        list_xml.append((res[0], res[1]))

    cursor.close()


def queryDicomMysql():
    path = '/home/tx-eva-data/PycharmProjects/deal-dicom-02/conf/mysql.ini'
    conn = conn_mysql.get_coon_tx(path)
    cursor = conn.cursor()
    sql =  "select B.label_path, D.remote_path from t_label_information as B join (select label_set_id, dicom_set_id from t_label_set where label_batch_id = (SELECT batch_id from t_batch_information where batch_name = '%s')) as A join t_dicom_information as D on A.label_set_id = B.Label_set_Id and A.dicom_set_id = D.collect_id" % '2019-12-31_DATA-1587'
    cursor.execute(sql)
    list_xml = []
    list_dicom = []
    for res in cursor.fetchall():
        list_xml.append(res[0])
        list_dicom.append(res[1])


    cursor.close()
    return list_xml, list_dicom








def post_data(value):

    endPointUrl = private_config.endPointUrl
    access_key = private_config.access_key
    secret_key = private_config.secret_key
    dcm_bucket, label_bucket = test_connection(endPointUrl, access_key, secret_key)
    out_path = private_config.out_path
    if str(value).endswith('.xml'):
        path = os.path.join(out_path, 'label')
        if not os.path.exists(path):
            os.mkdir(path)
        label_bucket.download_file(value, os.path.join(path, value.split('/')[-1]))
    else:
        path = os.path.join(out_path, 'dicom')
        if not os.path.exists(path):
            os.mkdir(path)
        dcm_bucket.download_file(value, os.path.join(path, value.split('/')[-1]))




if __name__ == '__main__':
    # list_label = queryLabelMysql()
    start = time.time()
    list_xml, list_dicom = queryDicomMysql()

    for ii in list_xml:
        post_data(ii)

    for dicom in list_dicom:
        post_data(dicom)
    print('程序运行完成', float(time.time() - start))

