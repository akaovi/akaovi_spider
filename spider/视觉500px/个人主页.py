# encoding : utf-8
# Author   : aka阿飞
# Datetime : 2021/8/18 16:11
# User     : AKA阿飞
# Product  : PyCharm
# Project  : pycharm
# File     : 个人主页.py

# 示例 https://500px.com.cn/Stuartphoto
import os

import time

import requests


class Shijue:
    def __init__(self):
        self.headers = {
            'Cookie': '',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73'
        }

    def add_file(self, path):
        """
        检验 path 是否有存在
        有则返回字符串 path
        反之创建并返回字符串 path
        """
        if not os.path.exists(path):
            os.mkdir(path)
        return path

    def get_uploaderId(self, one_img_url):
        json_url = f'{one_img_url}?type=json'
        json_data = requests.get(url=json_url, headers=self.headers).json()
        uploaderId = json_data['uploaderId']
        return uploaderId

    def img_download_1(self, img_id, uploaderId):
        img_url_1 = f'https://img.500px.me/{img_id}.jpg!p5'
        data = requests.get(url=img_url_1, headers=self.headers).content
        with open(self.add_file(f'C:/Users/AKA阿飞/Desktop/视觉500px/{uploaderId}') + '/' + f'{int(time.time()*100000)}.jpg', 'wb') as f:
            f.write(data)

    def img_dowanload_2(self, img_id, uploaderId):
        img_url = f'https://img.500px.me/photo/{uploaderId}/{img_id}.jpg!p5'
        img_data = requests.get(url=img_url, headers=self.headers).content
        with open(self.add_file(f'C:/Users/AKA阿飞/Desktop/视觉500px/{uploaderId}') + '/' + f'{int(time.time()*100000)}.jpg', 'wb') as f:
            f.write(img_data)

    def main(self, one_img_url, page):
        uploaderId = self.get_uploaderId(one_img_url)
        for i in range(1, page+1):
            try:
                json_url = f'https://500px.com.cn/community/v2/user/profile?resourceType=0,2,4&imgsize=p1,p2,p3&queriedUserId={uploaderId}&startTime=&page={i}&size=20&type=json'
                # print(json_url)
                json_data = requests.get(url=json_url, headers=self.headers).json()
                # print(json_data)
                images = json_data['data']
                # print(images)
                for img in images:
                    img_id = img['id']
                    # print(img_id)
                    if img_id[0:5] == '500px':
                        self.img_download_1(img_id, uploaderId)
                        print(f'{img_id}下载完毕!')
                    else:
                        self.img_dowanload_2(img_id, uploaderId)
                        print(f'{img_id}下载完毕!')
            except:
                return print('*'*10 + 'over!' + '*'*10)


if __name__ == "__main__":
    item = Shijue()
    one_img_url = 'https://500px.com.cn/community/photo-details/84cec3acf39e470aa98ce896112e15c7'
    item.main(one_img_url, 2)
    # 一般情况下，每页20张图片

# 有部分图片下载不成功
