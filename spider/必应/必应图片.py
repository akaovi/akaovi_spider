# -*- coding: utf-8 -*-
# encoding : utf-8
# Author   : aka阿飞
# Datetime : 2021/8/30 17:19
# User     : AKA阿飞
# Product  : PyCharm
# Project  : pycharm
# File     : 必应图片.py
import re

import httpx
import parsel
from retrying import retry


class Biyingimg:
    def __init__(self):
        self.headers = {
            'Referer': 'https://www.bingimg.cn/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84'
        }
        self.max_page = int(input('请输入爬取页数--->'))
        self.result_lst = []

    def parsel_(self):
        for page in range(1, self.max_page+1):
            url = f'https://www.nicebing.com/all?p={page}'
            resp = httpx.get(url=url, headers=self.headers)
            html = parsel.Selector(resp.text)
            images_id = html.xpath('//div[@class="col-md-4"]')
            for img_src in images_id:
                img = img_src.xpath('./div/img/@data-original').get()
                img = img.split('/')
                img = img[-3].replace('_1920x1080.jpg!', '')
                name = img_src.xpath('./div/div/p[1]/text()').get()
                name = re.sub('\(.*?\)', '', name).replace(' ', '')
                dic = {
                    name: img
                }
                self.result_lst.append(dic)
                print(dic)

    @retry(stop_max_attempt_number=3)
    def get_image_data(self, url):
        img_data = httpx.get(url=url, headers=self.headers).content
        return img_data

    def download(self):
        for img in self.result_lst:
            for key in img:
                print(f'--------->开始下载{key}<---------')
                download_url = f'https://www.bingimg.cn/down/uhd/{img[key]}_UHD.jpg'
                img_data = self.get_image_data(download_url)
                with open(f'C:/Users/AKA阿飞/Desktop/必应图片/{key}.jpg', 'wb') as f:
                    f.write(img_data)

    def run(self):
        print('---获取图片---')
        self.parsel_()
        print('---解析完毕，开始下载---')
        self.download()
        print('---数据保存完毕---')


if __name__ == "__main__":
    item = Biyingimg()
    item.run()

