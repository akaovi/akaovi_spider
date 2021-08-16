# encoding : utf-8
# Author   : aka阿飞
# Datetime : 2021/8/15 15:45
# User     : AKA阿飞
# Product  : PyCharm
# Project  : pycharm
# File     : 外汇.py
import parsel

import requests

import pymysql

class Exchange:
    def __init__(self):
        self.host = '127.0.0.1'
        self.user = 'root'
        self.password = '102419521abc'
        self.db = 'exchange'
        self.port = 3306
        self.charset = 'utf8'
        self.headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73'
}
        self.url = 'https://srh.bankofchina.com/search/whpj/search_cn.jsp'

    def connect(self):
        return pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db, port=self.port, charset=self.charset)

    def spider(self):
        """
        其它货币参照网址更换参数 --> pjname
        """
        lst1 = []
        for page in range(1, 6):
            params = {
                'pjname': '美元',
                'page': page
            }
            resp = requests.post(url=self.url, headers=self.headers, params=params)
            # print(resp.text, end='\n\n'+'*'*100+'\n\n')
            html = parsel.Selector(resp.text)
            # print(html)
            trs = html.xpath('//div[@class="BOC_main publish"]/table/tr')
            for tr_item in range(2, 22):
                value1 = trs.xpath(f'//tr[{tr_item}]/td[2]/text()').get()
                value2 = trs.xpath(f'//tr[{tr_item}]/td[3]/text()').get()
                value3 = trs.xpath(f'//tr[{tr_item}]/td[4]/text()').get()
                value4 = trs.xpath(f'//tr[{tr_item}]/td[5]/text()').get()
                value5 = trs.xpath(f'//tr[{tr_item}]/td[6]/text()').get()
                date = trs.xpath(f'//tr[{tr_item}]/td[7]/text()').get().replace('.', '-')
                lst1.append((float(value1), float(value2), float(value3), float(value4), float(value5), date))
        tuple_value = tuple(lst1)
        return tuple_value



if __name__=="__main__":
    item = Exchange()
    value = item.spider()
    conn = item.connect()
    cur = conn.cursor()
    stmt_insert = "INSERT INTO us_money (现汇买入价, 现钞买入价, 现汇卖出价, 现钞卖出价, 中行折算价, 发布时间) VALUES (%s, %s, %s, %s, %s, %s)"
    cur.executemany(stmt_insert, value)
    conn.commit()
    cur.close()
    conn.close()
