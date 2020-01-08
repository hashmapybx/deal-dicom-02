# coding=utf-8

import os
import sys
import boto3
import botocore
import requests
import json
from com.DR_test_download import private_config
from com.DR_test_download import conn_mysql
from multiprocessing import cpu_count, Process, JoinableQueue
import time
import pandas as pd


def test_connection(endPointUrl, verify, access_key, secret_key):
    s3 = boto3.resource(service_name='s3', aws_access_key_id=access_key,
                        aws_secret_access_key=secret_key, endpoint_url=endPointUrl,
                        verify=verify)
    dcm_bucket = s3.Bucket('dicom')
    label_bucket = s3.Bucket('label')


    return dcm_bucket, label_bucket




def download_list_all_dict(value, dcm_bucket, label_bucket, out_path):
    if str(value).endswith('.xml'):
        a_path = os.path.join(out_path, 'label', value.split('/')[-1][:-8])
        if not os.path.exists(a_path):
            os.makedirs(a_path)
        try:
            label_bucket.download_file(value, os.path.join(a_path, value.split('/')[-1]))
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == '404':
                print('the object does not exists')
                time.sleep(1)
                pass
            else:
                raise
    else:
        b_path = os.path.join(out_path, 'dicom', value.split('/')[-1][:-8])
        if not os.path.exists(b_path):
            os.makedirs(b_path)
        try:
            dcm_bucket.download_file(value, os.path.join(b_path, value.split('/')[-1]))
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == '404':
                print('the object does not exists')
                time.sleep(1)
                pass
            else:
                raise

def queryDicomMysql(batchName):
    path = '/home/tx-eva-data/PycharmProjects/deal-dicom-02/conf/mysql.ini'
    conn = conn_mysql.get_coon_tx(path)
    cursor = conn.cursor()
    sql =  "select B.label_path, D.remote_path from t_label_information as B join (select label_set_id, dicom_set_id from t_label_set where label_batch_id = (SELECT batch_id from t_batch_information where batch_name = '%s')) as A join t_dicom_information as D on A.label_set_id = B.Label_set_Id and A.dicom_set_id = D.collect_id" % batchName
    cursor.execute(sql)
    list_xml = []
    list_dicom = []
    for res in cursor.fetchall():
        list_xml.append(res[0])
        list_dicom.append(res[1])
    cursor.close()
    return list_xml, list_dicom



def Worker(q, dcm_bucket, label_bucket, out_path):
    while True:
        item = q.get()
        print(item)
        if item is None:
            break
        download_list_all_dict(item, dcm_bucket, label_bucket, out_path)
        q.task_done()



def producer(q, list_xml, list_dicom):

    for xml_file in list_xml:
        q.put(xml_file)
    for dcm_file in list_dicom:
        q.put(dcm_file)
    # # q.join()





def chulixmnl():
    path = '/media/tx-eva-data/Data4/DR_上线医院_test/data/tmp/label'
    list_a = []
    for sfile in os.listdir(path):
        a_folder = os.path.join(path, sfile)
        for ffile in os.listdir(a_folder):
            list_a.append(ffile)

    return list_a



if __name__ == '__main__':
    start = time.time()
    cpuCount = int(cpu_count())
    access_key = private_config.access_key
    secret_key = private_config.secret_key
    endPointUrl = private_config.endPointUrl
    # out_path = private_config.out_path
    batch_name = private_config.batchInformations[0]
    verify = False
    multiprocessing_list = []
    q = JoinableQueue()
    dcm_bucket, label_bucket = test_connection(endPointUrl, verify, access_key, secret_key)
    df = pd.read_csv('/home/tx-eva-data/Desktop/label.csv')
    xml_lists = list(df['label_path'].values)

    df1 = pd.read_csv('/home/tx-eva-data/Desktop/dicom.csv')
    dicom_lists = list(df1['remote_path'].values)



    out_path = '/media/tx-eva-data/Data4/DR_上线医院_test/data/a'

    producer(q, xml_lists, dicom_lists)

    for i in range(0, cpuCount):
        p = Process(target=Worker, args=(q, dcm_bucket, label_bucket, out_path,))
        p.daemon = True
        p.start()
        multiprocessing_list.append(p)
    for i in range(0, cpuCount):
        q.put(None)
    for p in multiprocessing_list:
        p.join()
    q.join()
    print("all work done")
    print('程序消耗的时间:', float(time.time() - start))


