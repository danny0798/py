# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 10:26:06 2017
@author: Administrator
"""

import requests
from bs4 import BeautifulSoup
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
}
total = []


def get_loupan(url):
    try:
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        titles = soup.find_all('span', class_='items-name')
        title = list(map(lambda x: x.text, titles))
        dizhis = soup.find_all('span', class_='list-map')
        dizhi = list(map(lambda x: x.text, dizhis))
        diqus = soup.find_all('span', class_='list-map')
        diqu = list(map(lambda x: x.text.split('\xa0')[1], diqus))
        mianjis_quan = soup.find_all('a', class_='huxing')
        mianji_quan = list(map(lambda x: x.text, mianjis_quan))
        mianjis = soup.find_all('a', class_='huxing')
        mianji = list(map(lambda x: x.text.split('\t')[-1].strip(), mianjis))
        jiages = soup.find_all('a', class_='favor-pos')
        jiage = list(map(lambda x: x.p.text, jiages))
        for tit, dizhi, diqu, mianq, mianj, jiage in zip(title, dizhi, diqu, mianji_quan, mianji, jiage):
            info = {'标题': tit,
                    '地址': dizhi,
                    '地区': diqu,
                    '面积（全）': mianq,
                    '面积': mianj,
                    '价格': jiage}
            total.append(info)
    except:
        print('')
    return total


if __name__ == '__main__':
    for i in range(1, 21):
        url = 'https://sh.fang.anjuke.com/loupan/all/p{}/'.format(i)
        get_loupan(url)
        print('第{}页抓取完毕'.format(i))
        time.sleep(1)
    import pandas as pd

    df = pd.DataFrame(total)
    df.to_excel('安居客.xls')


