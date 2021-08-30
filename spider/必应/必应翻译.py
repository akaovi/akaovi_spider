# -*- coding: utf-8 -*-
# encoding : utf-8
# Author   : aka阿飞
# Datetime : 2021/8/30 17:19
# User     : AKA阿飞
# Product  : PyCharm
# Project  : pycharm
# File     : 必应翻译.py
import time

from selenium import webdriver


class Biyingfanyi:
    def __init__(self):
        self.word = input('请输入要查询的单词--->')
        self.EDGE = {
            "browserName": "MicrosoftEdge",
            "version": "",
            "platform": "WINDOWS",
            "ms:edgeOptions": {
                'extensions': [],
                'args': [
                    '--headless',
                    '--disable-gpu'
                ]}
        }
        self.driver = webdriver.Edge(executable_path=r'F:\下载\msedgedriver.exe', capabilities=self.EDGE)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def parsel_(self):
        url = f'https://cn.bing.com/dict/search?q={self.word}'
        self.driver.get(url)
        t1 = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[1]/ul')
        t2 = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[1]/div[2]')
        print(t1.text)
        print(t2.text)
        time.sleep(0.05)
        self.driver.quit()

    def run(self):
        self.parsel_()


if __name__ == "__main__":
    item = Biyingfanyi()
    item.run()

