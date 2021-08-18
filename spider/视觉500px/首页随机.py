# encoding : utf-8
# Author   : aka阿飞
# Datetime : 2021/8/18 11:21
# User     : AKA阿飞
# Product  : PyCharm
# Project  : pycharm
# File     : 社区.py

# json数据
# https://500px.com.cn/feedflow/index?startTime=&page=1&size=21

# https://img.500px.me/500px1035957274.jpg!p5
# https://img.500px.me/{id}.jpg!p5

# img_url https://img.500px.me/photo/d22c8bd90498191760494f5bdfcb59371/4ce47cb7fdc6497c94ad87c0c9d8094a.jpeg!p5
import time

import requests


class Shijue:
    def __init__(self):
        self.url = 'https://500px.com.cn/community/index.html'
        self.headers = {
            'Referer': self.url,
            'Cookie': '',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73',
            # 'X-Requested-With': 'XMLHttpRequest',
            # 'X-Tingyun-Id': 'Fm3hXcTiLT8;r=54643887'
        }

    def img_download_1(self, img_id):
        img_url_1 = f'https://img.500px.me/{img_id}.jpg!p5'
        data = requests.get(url=img_url_1, headers=self.headers).content
        with open('C:/Users/AKA阿飞/Desktop/视觉500px/' + f'{int(time.time()*100000)}.jpg', 'wb') as f:
            f.write(data)

    def img_download_2(self, uploaderId, resourceId):
        img_url_2 = f'https://img.500px.me/photo/{uploaderId}/{resourceId}.jpg!p5'
        data = requests.get(url=img_url_2, headers=self.headers).content
        with open('C:/Users/AKA阿飞/Desktop/视觉500px/' + f'{int(time.time() * 100000)}.jpg', 'wb') as f:
            f.write(data)


    def main(self):
        json_url = 'https://500px.com.cn/feedflow/index?startTime=&page=1&size=21'
        json_data = requests.get(url=json_url, headers=self.headers).json()
        for data in json_data['data']:
            img_id = data['id']
            if img_id[0:5] == '500px':
                self.img_download_1(img_id)
                print(f'{img_id}下载完毕!')
            else:
                uploaderId = data['uploaderId']
                resourceId = data['url']['id']
                self.img_download_2(uploaderId, resourceId)
                print(f'{img_id}下载完毕!')


if __name__ == "__main__":
    item = Shijue()
    item.main()

# json内存在id 但是会报错不存在  emmm不懂

