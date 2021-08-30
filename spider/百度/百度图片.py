# -*- coding: utf-8 -*-
# encoding : utf-8
# Author   : aka阿飞
# Datetime : 2021/8/30 14:30
# User     : AKA阿飞
# Product  : PyCharm
# Project  : pycharm
# File     : 百度图片.py
import time

import httpx
import parsel
from selenium import webdriver


class Baidutupian:
    def __init__(self):
        self.word = input('请输入搜索关键词--->')
        self.times = int(input('请输入下载页数，如2--->'))
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84'
        }
        self.driver = webdriver.Edge(r'F:\下载\msedgedriver.exe')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def login(self):
        pass

    def parsel_(self):
        print('---开始解析网页---')
        url = f'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&fm=index&pos=history&word={self.word}'
        self.driver.get(url)
        for page in range(self.times):
            self.driver.execute_script('window.scrollTo(0, 5000)')
            time.sleep(0.5)
        html_page = self.driver.page_source
        html = parsel.Selector(html_page)
        print('---开始保存图片---')
        lis = html.xpath('//div[@class="imgpage"]//li/@data-objurl').extract()
        for i in lis[2:]:
            self.download(i)
        self.driver.quit()

    def download(self, url):
        with open(r'C:\Users\AKA阿飞\Desktop\百度图片\{}.jpg'.format(int(time.time()*100000)), 'wb') as f:
            resp = httpx.get(url=url, headers=self.headers).content
            f.write(resp)

    def run(self):
        self.parsel_()
        print('---结束运行---')


if __name__ == "__main__":
    item = Baidutupian()
    item.run()

