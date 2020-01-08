# -*- coding: utf-8 -*-
"""
Create Time: 2019/11/8 下午5:47
Author: ybx
"""
import pymysql
import configparser
from multiprocessing import Process, Queue

def get_conn_localhost():
    conn = pymysql.connect(
        host="localhost",
        user='root',
        password='123456',
        database='Mysite',
        charset='utf-8',
    )
    return conn


def get_coon_tx(path):
    # 需要穿进去配置文件路径
    cf = configparser.ConfigParser()
    cf.read(path)
    # sections = cf.sections() # 返回list
    items = cf.items("mysql_local")
    d_conf = dict(items)
    d_conf['port'] = int(d_conf['port'])
    conn = pymysql.connect(**d_conf)
    return conn


'''
需要开发模块来下载相应的数据
'''

# def main():
#     path = '/media/tx-eva-data/Data1/pycharmproject/mysite/conf/mysql.ini'
#     conn = get_coon_tx(path)
#     cursor = conn.cursor()
#     #想要下载没有label的数据的话 必须根据数据库中t_dicom_information 里面的dicom_path的信息 爱boto3 里面的ducket('dicom')里面进行下载操作
#
#     ruku_date = ''
#     hosp_number = ''
#     sql = "select remote_path from t_dicom_information where create_date = '%s' and b '%s' " % (ruku_date, hosp_number)
#     result = cursor.execute(sql)
#     cursor.close()
#     # 遍历该批次的所有dicom信息 保存到list里面 在遍历 利用多进程去进行下载dicom数据




# if __name__ == '__main__':
#     path = '/media/tx-eva-data/Data1/pycharmproject/mysite/conf/mysql.ini'
#     dd = get_coon_tx(path)
#     print(dd)