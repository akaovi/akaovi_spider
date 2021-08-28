# -*- coding: utf-8 -*-
# encoding : utf-8
# Author   : aka阿飞
# Datetime : 2021/8/28 20:06
# User     : AKA阿飞
# Product  : PyCharm
# Project  : pycharm
# File     : 猫眼实时监测票房.py
import re
import time

import httpx


class Maoyan:
    def __init__(self):
        self.headers = {
            'Referer': 'https://piaofang.maoyan.com/dashboard',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84'
        }
        self.result_lst = []

    def parsel_(self):
        json_url = 'https://piaofang.maoyan.com/dashboard-ajax?orderType=0&uuid=17b8b8305a1c8-0c37181d4560f6-7068776a-144000-17b8b8305a2c8'
        json_data = httpx.get(url=json_url, headers=self.headers).json()
        num = json_data['movieList']['data']['nationBoxInfo']['nationBoxSplitUnit']['num']
        movie_lst = json_data['movieList']['data']['list']
        for lst in movie_lst:
            boxRate = lst['boxRate']  # 票房占比
            boxRate = re.findall('\d+\.\d+', boxRate)[0]
            movieName = lst['movieInfo']['movieName']
            releaseInfo = lst['movieInfo']['releaseInfo']
            showCount = lst['showCount']
            sumbox = float(num) * float(boxRate)
            dic = {
                '电影名称:': movieName,
                '综合票房:': sumbox,
                '上映天数:': releaseInfo,
                '排片场次:': showCount
            }
            self.result_lst.append(dic)

    def run(self):
        while True:
            self.parsel_()
            for i in self.result_lst:
                print(i)
            print('\n')
            self.result_lst = []
            time.sleep(3)


if __name__ == "__main__":
    item = Maoyan()
    item.run()

