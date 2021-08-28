# -*- coding: utf-8 -*-
# encoding : utf-8
# Author   : aka阿飞
# Datetime : 2021/8/28 21:01
# User     : AKA阿飞
# Product  : PyCharm
# Project  : pycharm
# File     : 安居客.py
import httpx
import parsel


class Anjuke:
    def __init__(self):
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84'
        }
        self.page_max = input('请输入爬取页数--->')
        self.result_lst = []
        self.keyword = input('请输入搜索关键词--->')

    def parsel_(self):
        for page in range(1, int(self.page_max)+1):
            print(f'---正在获取第{page}页数据---')
            url = f'https://chongqing.anjuke.com/sale/p{page}/?q={self.keyword}'
            resp = httpx.get(url=url, headers=self.headers)
            # print(resp.text)
            html = parsel.Selector(resp.text)
            all_lst = html.xpath('//div[@tongji_tag="fcpc_ersflist_gzcount"]')
            for house in all_lst:
                href = house.xpath('./a/@href').get()
                title = house.xpath('./a//h3/text()').get()
                d1 = house.xpath('.//section/div[1]//text()').extract()
                d1 = ''.join(d1).replace(' ', '').replace('\n', '  ')
                d2 = house.xpath('.//section/div[2]//text()').extract()
                d2 = ''.join(d2).replace(' ', '').replace('\n', '  ')
                d3 = house.xpath('.//section/div[3]/span/text()').extract()
                d3 = '  '.join(d3)
                info = title + '\n' + d1 + '\n' + d2 + '\n' + d3 + '\n' + href + '\n\n'
                self.result_lst.append(info)



    def download(self):
        print('---开始保存数据---')
        with open('./{安居客房屋数据}.txt', 'wb') as f:
            for info in self.result_lst:
                f.write(bytes(info, encoding='utf-8'))

    def run(self):
        self.parsel_()
        print('---数据获取完毕---')
        self.download()
        print('---数据保存完毕---')


if __name__ == "__main__":
    item = Anjuke()
    item.run()

