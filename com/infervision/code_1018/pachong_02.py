# -*- coding: utf-8 -*-
"""
Create Time: 2019/10/22 下午6:29
Author: ybx
"""

import requests
import urllib.request
import json
from lxml import etree
import re
import os
from bs4 import BeautifulSoup
import  random


headers={

"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
}

def get_one_page(url):
    response = urllib.request.urlopen(url)
    text = response.read().decode('utf-8')
    return text


def get_url(offset, i):
    proxy = '183.164.238.32:9999|27.43.187.59:9999|121.226.188.162:9999'
    proies = {
        'http': 'http://' + proxy.split('|')[random.randint(0, 2)],
        'https': 'https://' + proxy.split('|')[random.randint(0, 2)]
    }
    url = 'https://data.tbportals.niaid.nih.gov/cases?_take='+str(offset)+'&_skip='+str(offset * i)
    r = requests.get(url, headers=headers, timeout=100)
    demo = r.text  # 服务器返回响应
    # soup = BeautifulSoup(demo, "html.parser")
    fout = open('/media/tx-eva-data/Data1/dailyFile/download/html/%s.txt' % str(offset)+'_'+str(i), 'a')
    fout.write(demo)
    fout.close()
    # p_all = soup.find_all(name='p', attrs={'class': "text-uppercase"})
    # list_a = [] # 记录每一个病人的ID
    # for p in p_all:
    #     patient_id = str(p.text)
    #     if patient_id.isdigit():
    #         list_a.append(patient_id)
    # print(len(list_a))
    # a_all = soup.find_all('a')
    # # print(a_all)
    # pid_case = set()
    # for a in a_all:
    #     try:
    #         href = a.attrs['href']
    #     except:
    #         pass
    #     if str(href).startswith('/patient/'):
    #         # print(href)
    #         pid_case.add('https://data.tbportals.niaid.nih.gov/'+href)
    # fout = open('/home/tx-eva-data/PycharmProjects/deal-dicom-02/com/infervision/code_1018/url.txt', 'a')
    # for url_a in pid_case:
    #     fout.write(url_a + '\n')
    #
    # fout.close()


def get_url_2():
    list_case_detail = get_url()
    for value in list_case_detail:
        r = requests.get(value)
        demo = r.text  # 服务器返回响应
        soup = BeautifulSoup(demo, "html.parser")
        pid = soup.find('h5', attrs={'class': 'text-uppercase'}).text
        print(pid)




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
                pid = pid[8:]
                path = pid[29:]
                a_path = os.path.split(path)[0]
                insatnce_name = os.path.split(path)[-1]
                # print(a_path)
                out_path = os.path.join(save_path, a_path)
                if not os.path.exists(out_path):
                    os.makedirs(out_path)
                urllib.request.urlretrieve(pid, os.path.join(save_path, insatnce_name))
                print('download')



if __name__ == '__main__':
    # main()
    # get_url()
    for i in range(111):
        get_url(21, i)


