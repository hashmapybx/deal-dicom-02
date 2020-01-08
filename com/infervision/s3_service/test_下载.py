# -*- coding: utf-8 -*-
"""
Create Time: 2019/11/25 下午5:02
Author: ybx
"""

import boto3

import os
import time
import random
import datetime
from multiprocessing import Process, Queue
from com.infervision.s3_service import connect_mysql


def test_connection(endPointUrl, verify, access_key, secret_key):
    s3 = boto3.resource(service_name='s3', aws_access_key_id=access_key,
                        aws_secret_access_key=secret_key, endpoint_url=endPointUrl,
                        verify=verify)

    dcm_bucket = s3.Bucket('dicom')
    return dcm_bucket


def readMysql(q):
    # 从mysql里面去获取数据操作
    path = '/home/tx-eva-data/PycharmProjects/deal-dicom-02/conf/mysql.ini'
    create_time = '2019-11-27'
    conn = connect_mysql.get_coon_tx(path)
    cursor = conn.cursor()
    try:
        sql = "select name from student where create_date like '%2019-11-27%' "
        cursor.execute(sql)
        result = cursor.fetchall()  # 获取返回的所有的数据
        for row in result:
            q.put(row)

        # cursor.fetchone() # 获取返回的一条数据的操作
        # cursor.fetchmany(3) # 获取返回结果的前三行数据
    except Exception as e:
        print('Error')

    cursor.close()
    conn.close()


def generte_dtci():
    dict_a = {

        'uuid': str(random.randint(0000, 9999)).zfill(10),
        'name': 'tom_' + str(random.randint(0000, 9999)).zfill(6),
        'age': random.randint(0, 99),
        'create_date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    return dict_a


def mysql_insert():
    '''
    为了写入一个通用的 sql插入操作 需要构造一个字典 用于在数据插入的时候去使用
    :return:
    '''
    path = '/home/tx-eva-data/PycharmProjects/deal-dicom-02/conf/mysql.ini'
    data = generte_dtci()
    table = 'student'
    keys = ','.join(data.keys())
    values = ','.join(['%s'] * len(data))
    conn = connect_mysql.get_coon_tx(path)
    cursor = conn.cursor()
    sql = 'insert into {table}({keys}) values ({values})'.format(table=table, keys=keys, values=values)
    try:
        if cursor.execute(sql, tuple(data.values())):
            print('successful')
            conn.commit()
    except:
        print('failed')
        conn.rollback()

    cursor.close()
    conn.close()



def mysql_insert_piliang():
    '''
    为了写入一个通用的 sql插入操作 需要构造一个字典 用于在数据插入的时候去使用
    :return:
    '''
    path = '/home/tx-eva-data/PycharmProjects/deal-dicom-02/conf/mysql.ini'
    data = generte_dtci()
    table = 'student'
    keys = ','.join(data.keys())
    values = ','.join(['%s'] * len(data))
    conn = connect_mysql.get_coon_tx(path)
    cursor = conn.cursor()
    sql = 'insert into {table}({keys}) values ({values})'.format(table=table, keys=keys, values=values)
    try:
        if cursor.execute(sql, tuple(data.values())):
            print('successful')
            conn.commit()
    except:
        print('failed')
        conn.rollback()

    cursor.close()
    conn.close()





def downloadDicom(list, dcm_bucket):
    for dcm_path in list:
        file_path = os.path.dirname(__file__)
        dcm_bucket.download_file(dcm_path, os.path.join(file_path, dcm_path.split('/')[-1]))
    print('download file')



def Worker(q, dcm_bucket):
    print('test')
    while 1:
        dcm_path = q.get()
        if not (dcm_path is None):
            file_path = os.path.dirname(__file__)
            out_path = os.path.join(file_path, dcm_path.split('/')[-1][:-8])
            if not os.path.exists(out_path):
                os.makedirs(out_path)
            dcm_bucket.download_file(dcm_path, os.path.join(out_path, dcm_path.split('/')[-1]))




def worker1(q):
    print('开始消费数据了')
    while 1:
        stu_name = q.get()

        print('父进程id: %d,消费者id: %d, 数据是: %s' % (os.getppid(), os.getpid(), stu_name))



def main():
    '''连接S3用户名及密钥'''
    # access_key = "Y37DCO4238IH7VFLQSGW"
    # secret_key = "NJXRbEX2lFXoP5IB15TrykRZQnvg8KR3qz9AgbBc"
    #
    # '''连接到数据库接口和Ｓ3地址'''
    # endPointUrl = "http://192.168.130.82:7480"
    # url = "http://192.168.130.81:8096/acquire/"
    # verify = False
    # dcm_bucket = test_connection(endPointUrl, verify, access_key, secret_key)

    # 此时需要多进程异步完成操作
    q = Queue()

    # 生产者
    '''
    这里存在问题的当生产者是多个的时候 每一个生产者都回去执行一遍数据库查询操作 消费者消费的数据就是会存在重复的现象
    '''


    list_writer = []
    for i in range(1):
        p = Process(target=readMysql, args=(q,))
        p.start()
        list_writer.append(p)
    # 消费者
    list_reader = []
    for i in range(5):
        p = Process(target=worker1, args=(q,))
        p.start()
        list_reader.append(p)
    for a in list_writer:
        a.join()

    # 下面是去关闭消费者进程资源
    for j in list_reader:
        j.terminate()





if __name__ == '__main__':
    # print(os.path.dirname(__file__))
    start = time.time()
    main()
    # for i in range(0, 1000):
    #     mysql_insert()

    print((time.time() - start))
