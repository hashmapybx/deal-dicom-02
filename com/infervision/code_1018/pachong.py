# -*- coding: utf-8 -*-
"""
Create Time: 2019/10/22 下午4:01
Author: ybx
"""
import requests
import urllib.request
import json
from lxml import etree
import re
import os

def get_one_page(url):

    response = urllib.request.urlopen(url)
    text = response.read().decode('utf-8')
    return text



def main():
    save_path = "/media/tx-eva-data/Data1/dailyFile/download"
    url = 'https://data.tbportals.niaid.nih.gov/patient/1ff29035-0e5c-43d3-ab1d-63598f5053a3/case/c7edaeb1-6b28-449c-ab3d-1805bb75b4e0/imaging/view/4d30803d-f6f7-4c01-a5e1-54b999016f57'
    text = get_one_page(url)

    htmlinfo = etree.HTML(text)
    for person in htmlinfo.xpath('//script/text()'):
        if 'studyContainer' in str(person):
            result = re.compile("\{.*\}")
            dict_str = result.search(str(person))[0]
            res = json.loads(dict_str)
            list_a = res['series'][0]['instance']
            for pid in list_a:
                pid= pid[8:]
                path = pid[29:]
                a_path = os.path.split(path)[0]
                insatnce_name = os.path.split(path)[-1]
                # print(a_path)
                out_path = os.path.join(save_path, a_path)
                if not os.path.exists(out_path):
                    os.makedirs(out_path)
                urllib.request.urlretrieve(pid, os.path.join(save_path, insatnce_name))
                print('download')




def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')



main()


