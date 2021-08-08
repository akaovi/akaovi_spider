import datetime
import os

import requests

def titlename():
    """
    获取上一天时间作为文件名
    """
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    datetoday = str(yesterday).split('-')
    date = ''
    for i in datetoday:
        date += i
    return date


headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.63'
        }

name = titlename()

path = 'C:/Users/AKA阿飞/Desktop/p站每日一爬/' + name + '/'

# 创建文件夹
os.mkdir(path)

for i in [0, 30, 60, 90, 120]:
    try:
        realpath = path + str(i) + '/'
        os.mkdir(realpath)
        url = f'https://www.vilipix.com/api/illust?mode=daily&date={name}&limit=30&offset={i}'
        response = requests.get(url=url, headers=headers).json()
        for i in range(0, 30):
            regular_url = response['rows'][i]['regular_url']
            jpg = requests.get(url=regular_url, headers=headers).content
            with open(realpath + str(i) + '.jpg', mode='wb') as f:
                    f.write(jpg)
    except:
        continue
