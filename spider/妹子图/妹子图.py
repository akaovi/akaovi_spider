# -*- coding: utf-8 -*-
# encoding : utf-8
# Author   : aka阿飞
# Datetime : 2021/8/27 20:30
# User     : AKA阿飞
# Product  : PyCharm
# Project  : pycharm
# File     : 妹子图.py

# https://www.mzitu.com/page/2/
import os
import time

import requests
import parsel


class Meizitu:
    def __init__(self):
        self.headers = {
            'Referer': 'https://www.mzitu.com/',  # 反扒
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.78'
        }
        # self.page_max = 1
        self.page_max = input('--->请输入爬取页数-->')
        self.dic_lst = []

    def add_file(self, path):
        """
        检验 path 是否有存在
        有则返回字符串 path
        反之创建并返回字符串 path
        """
        if not os.path.exists(path):
            os.mkdir(path)
        return path

    def parsel_(self):
        for page in range(1, int(self.page_max)+1):
            meizitu_url = f'https://www.mzitu.com/page/{page}/'
            resp = requests.get(url=meizitu_url, headers=self.headers)
            html = parsel.Selector(resp.text)
            li_lst = html.xpath('//*[@id="pins"]/li')
            for li in li_lst:
                dic = {
                    'href': li.xpath('./a/@href').get(),
                    'title': li.xpath('./span[2]/text()').get() + li.xpath('./span[1]/a/text()').get()
                }
                self.dic_lst.append(dic)

    def download(self):
        for dic in self.dic_lst:
            self.add_file(f'C:/Users/AKA阿飞/Desktop/妹子图/{dic["title"]}')
            resp = requests.get(url=dic['href'], headers=self.headers)
            html = parsel.Selector(resp.text)
            page_max = html.xpath('//div[@class="pagenavi"]/a[5]/span/text()').get()
            for page in range(1, int(page_max)):
                url_ = dic['href'] + f'/{page}'
                img_resp = requests.get(url=url_, headers=self.headers)
                img_html = parsel.Selector(img_resp.text)
                img_url = img_html.xpath('//div[@class="main-image"]/p/a/img/@src').get()
                img_data = requests.get(url=img_url, headers=self.headers).content
                with open(f'C:/Users/AKA阿飞/Desktop/妹子图/{dic["title"]}/{int(time.time()*100000)}.jpg', 'wb') as f:
                    f.write(img_data)

    def run(self):
        print('~~~正在获取图片~~~')
        self.parsel_()
        print('~~~正在保存图片~~~')
        self.download()
        print('~~~程序结束~~~')


if __name__ == "__main__":
    item = Meizitu()
    item.run()

