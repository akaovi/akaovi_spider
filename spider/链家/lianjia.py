# -*- coding: utf-8 -*-
# encoding : utf-8
# Author   : aka阿飞
# Datetime : 2021/9/12 16:40
# User     : AKA阿飞
# Product  : PyCharm
# Project  : WeiboAPI
# File     : get.py
import time
import httpx
import parsel
import pandas as pd


class Lianjia:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.44'
        }

    def parsel_(self):
        data_lst = []
        for page in range(1, 101):
            get_url = f'https://cq.lianjia.com/ershoufang/pg{page}/'
            resp_text = httpx.get(url=get_url, headers=self.headers).text
            html = parsel.Selector(resp_text)
            lis = html.xpath('//*[@id="content"]/div[1]/ul/li')
            for li in lis:
                data_dic = {
                    'title': li.xpath('.//div[@class="title"]/a/text()').get(),
                    'totalPrice': ''.join(li.xpath('.//div[@class="priceInfo"]/div[1]//text()').extract()).replace(' ', ''),
                    'unitPrice': li.xpath('.//div[@class="priceInfo"]/div[2]/span/text()').get(),
                    'span': li.xpath('.//div[@class="title"]/span/text()').get(),
                    'flood': li.xpath('.//div[@class="flood"]/div/a/text()').get(),
                    'address': li.xpath('.//div[@class="address"]//text()').get(),
                    'followInfo': li.xpath('.//div[@class="followInfo"]/text()').get(),
                    'tag': ','.join(li.xpath('.//div[@class="tag"]/span/text()').extract()),
                    'url': li.xpath('.//div[@class="title"]/a/@href').get()
                }
                data_lst.append(data_dic)
            time.sleep(1)
        return data_lst

    def run(self):
        data_lst = self.parsel_()
        df = pd.DataFrame(data_lst)
        df.to_csv('exc.csv', encoding='utf_8_sig')


if __name__ == '__main__':
    item = Lianjia()
    item.run()

