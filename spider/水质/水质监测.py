# -*- coding: utf-8 -*-
# encoding : utf-8
# Author   : aka阿飞
# Datetime : 2021/8/28 17:29
# User     : AKA阿飞
# Product  : PyCharm
# Project  : pycharm
# File     : 水质数据.py

# http://106.37.208.243:8068/GJZ/Business/Publish/Main.html

# http://106.37.208.243:8068/GJZ/Ajax/Publish.ashx
import re
import time

import httpx
import xlwt


class Shuizhi:
    def __init__(self):
        self.headers = {
            'Referer': 'http://106.37.208.243:8068/GJZ/Business/Publish/RealDatas.html',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84'
        }
        # self.page_max = 3
        self.page_max = int(input('--->请输入爬取页数--->'))
        self.result_lst = []

    def parsel_(self):
        post_url = 'http://106.37.208.243:8068/GJZ/Ajax/Publish.ashx'
        for page in range(1, self.page_max+1):
            print(f'---正在获取第{page}页的数据---')
            time.sleep(2)
            print('慢慢来，别被封禁了~~~')
            data = {
                'AreaID': '',
                'RiverID': '',
                'MNName': '',
                'PageIndex': page,
                'PageSize': 60,
                'action': 'getRealDatas'
            }
            json_data = httpx.post(url=post_url, headers=self.headers, data=data).json()
            result = json_data['tbody']
            for lst in result:
                self.result_lst.append(lst)

    def download(self):
        book = xlwt.Workbook(encoding='utf-8')
        sheet = book.add_sheet('水质监测', cell_overwrite_ok=True)

        sheet.write(0, 0, '省份')
        sheet.write(0, 1, '流域')
        sheet.write(0, 2, '断面名称')
        sheet.write(0, 3, '监测时间')
        sheet.write(0, 4, '水质类别')
        sheet.write(0, 5, '水温(℃)')
        sheet.write(0, 6, 'pH(无量纲)')
        sheet.write(0, 7, '溶解氧(mg/L)')
        sheet.write(0, 8, '电导率(μS/cm)')
        sheet.write(0, 9, '浊度(NTU)')
        sheet.write(0, 10, '高锰酸盐指数(mg/L)')
        sheet.write(0, 11, '氨氮(mg/L)')
        sheet.write(0, 12, '总磷(mg/L)')
        sheet.write(0, 13, '总氮(mg/L)')
        sheet.write(0, 14, '叶绿素α(mg/L)')
        sheet.write(0, 15, '藻密度(cells/L)')
        sheet.write(0, 16, '站点情况')

        r = 1
        for lst in self.result_lst:
            row = sheet.row(r)
            c = 0
            for value in lst:
                if type(value) == str:
                    value = re.sub("<span.*?title='", '', value)
                    value = re.sub("'>.*?>", '', value).replace('&#10;', ' ')
                row.write(c, value)
                c += 1
            r += 1

        book.save('水质.xls')

    def run(self):
        print('---正在获取数据---')
        self.parsel_()
        print('---正在保存数据---')
        # print(self.result_lst)
        self.download()
        print('---数据保存完毕---')


if __name__ == "__main__":
    item = Shuizhi()
    item.run()

