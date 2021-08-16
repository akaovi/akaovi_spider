# encoding : utf-8
# Author   : aka阿飞
# Datetime : 2021/8/16 16:44
# User     : AKA阿飞
# Product  : PyCharm
# Project  : pycharm
# File     : 精选页面.py
import os

import time

import requests


class Tuchong:
    def __init__(self):
        # https://tuchong.com/rest/categories/精选/recommend?categoryName=精选&type=next&last_post_id={}
        self.url = 'https://tuchong.com/rest/categories/精选/recommend'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67',
            'cookie': 'ttcid=a6884820cd3c43e3ad12b80c84f5342742; log_web_id=5286238400; wluuid=WLGEUST-9B11240F-82EC-AF82-B088-931C9810FAD4; ssoflag=0; wlsource=tc_pc_home_search; __utmz=115147160.1618918335.4.2.utmcsr=tuchong.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _ga=GA1.2.694931593.1618413531; PHPSESSID=ju1tukodb1oiuqmc253dt0csed; lang=zh; creative_device_id=fc4cbd43-caf8-4970-843f-55250e6c33f9; creative_token=eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2MjkwOTk5NzYsInZhbCI6IkZWSzdJU0JKUE9PV0ZGRFVaSlVSM0FPVzcyT0pUQ0I2QTQ0VVFVQ0xJNE1LSDVaRkZZRVEifQ.q2gpR7OtZ_bGqabwLDYlJbJToKwwxYL6JNefNNqemkFBwRvSvmbqwY1GYZzsT9Ao; source=adobe; token=f54c79b50f97afdd; _gid=GA1.2.956620156.1629101618; __utma=115147160.694931593.1618413531.1622365801.1629101618.6; __utmc=115147160; __utmb=115147160.1.10.1629101618; s_v_web_id=verify_ksed1hm3_AM5NLCWI_g3Cj_4TOl_A9q4_1eQafEdjlTRB; MONITOR_WEB_ID=24894185; webp_enabled=1; tt_scid=lfp8EAhqtGKLDG8H6B9PLGwXftOQlsFcokz95SDD1eIoxLkhpJvSFyK91mu20wF18d03'
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

    def download(self, author_id, img_id):
        """

        """
        url = f'https://photo.tuchong.com/{author_id}/f/{img_id}.jpg'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67',
        }
        data = requests.get(url=url, headers=headers).content
        with open(self.add_file(f'C:/Users/AKA阿飞/Desktop/图虫/{author_id}') + '/' + f'{int(time.time() * 1000000)}.jpg', 'wb') as f:
            f.write(data)

    def req(self, last_post_id=None):
        """

        """
        if last_post_id == None:
            resp = requests.get(url=self.url, headers=self.headers)
        else:
            url = f'https://tuchong.com/rest/categories/精选/recommend?categoryName=精选&type=next&last_post_id={last_post_id}'
            resp = requests.get(url=url, headers=self.headers)
        # print(resp.json())
        json_data = resp.json()
        all_author = json_data['feedList']
        last_post_id = all_author[-1]['post_id']
        # print(last_post_id)
        for author in all_author:
            author_id = author['author_id']
            # print(author_id)
            images = author['images']
            for img in images:
                img_id = img['img_id']
                # print(img_id)
                self.download(author_id, img_id)
        return last_post_id


if __name__ == '__main__':
    item = Tuchong()
    last_post_id = None
    for i in range(3):
        last_post_id = item.req(last_post_id)
