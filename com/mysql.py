# -*- coding: utf-8 -*-
"""
Create Time: 2019/12/12 下午1:02
Author: ybx
"""
import configparser
import pymysql
def get_coon_tx(path):
    # 需要穿进去配置文件路径
    cf = configparser.ConfigParser()
    cf.read(path)
    sections = cf.sections()  # 返回list
    items = cf.items("mysql_tx")
    d_conf = dict(items)
    d_conf['port'] = int(d_conf['port'])
    conn = pymysql.connect(**d_conf)
    return conn




def query():
    path = '/home/tx-eva-data/PycharmProjects/deal-dicom-02/conf/mysql.ini'
    conn = get_coon_tx(path)
    cursor = conn.cursor()
    sql = "select * from "