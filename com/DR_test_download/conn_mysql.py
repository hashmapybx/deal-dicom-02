# -*- coding: utf-8 -*-
"""
Create Time: 2020/1/2 下午2:30
Author: ybx
"""
import pymysql
import configparser


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