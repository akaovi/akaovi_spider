# -*- coding: utf-8 -*-
# encoding : utf-8
# Author   : aka阿飞
# Datetime : 2021/9/5 11:17
# User     : AKA阿飞
# Product  : PyCharm
# Project  : 实例
# File     : 必应图片搜索.py
import time

import httpx
from selenium import webdriver


class BingPicture:
    def __init__(self):
        self.keyword = input('请输入搜索关键词--->')
        self.picture_lst = []
        self.driver = webdriver.Edge(executable_path=r'F:\下载\msedgedriver.exe')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def parsel_(self):
        url = f'https://cn.bing.com/images/search?q={self.keyword}&form=QBIR&first=1&tsc=ImageHoverTitle'
        self.driver.get(url)
        js = 'window.scrollTo(0, 5000)'
        for times in range(7):
            self.driver.execute_script(js)
            time.sleep(0.5)
        print('---解析数据---')
        lis = self.driver.find_elements_by_xpath('//*[@class="dgControl_list"]/li')
        for li in lis:
            m = li.find_element_by_xpath('.//div[@class="imgpt"]/a').get_attribute('m')
            self.picture_lst.append(eval(m)['murl'])
        self.driver.quit()
        # print(self.picture_lst)

    def download(self):
        print('---开始保存数据---')
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.38'
        }
        for url in self.picture_lst:
            try:
                img_data = httpx.get(url=url, headers=headers, timeout=5).content
                with open(f'C:/Users/AKA阿飞/Desktop/必应图片/{int(time.time()*100000)}.jpg', 'wb') as f:
                    f.write(img_data)
            except:
                continue
        print('---数据保存完毕---')

    def run(self):
        self.parsel_()
        self.download()


if __name__ == "__main__":
    item = BingPicture()
    item.run()

