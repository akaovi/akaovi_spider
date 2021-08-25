# encoding : utf-8
# Author   : aka阿飞
# Datetime : 2021/8/25 14:22
# User     : AKA阿飞
# Product  : PyCharm
# Project  : pycharm
# File     : 笔趣阁.py

"""
传入下载的小说目录页
"""

# 官网 https://www.biqooge.com/
import os
import httpx
import parsel
from retrying import retry


class Biquge:
    def __init__(self):
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.78'
        }
        self.url_lst = {}
        self.title = None
        self.author = None
        self.details = None
        self.proxy = {
            'http': ''
            'httpx': ''
        }

    def add_file(self, path):
        """
        检验 path 是否有存在
        有则返回字符串 path
        反之创建并返回字符串 path
        """
        if not os.path.exists(path):
            os.mkdir(path)
        return path

    @retry(stop_max_attempt_number=3)
    def single_page_prs(self, page_url):
        resp = httpx.get(url=page_url, headers=self.headers, timeout=5)
        resp.encoding = 'gbk'
        # print(resp.text)
        html = parsel.Selector(resp.text)
        contents = html.xpath('//*[@id="content"]').xpath('string(.)').extract()[0]
        # print(contents)
        return bytes(contents, encoding='utf-8')

    def download(self):
        self.add_file(f'C:/Users/AKA阿飞/Desktop/笔趣阁/{self.title}')

        # 简介
        with open(f'C:/Users/AKA阿飞/Desktop/笔趣阁/{self.title}/简介details---避免重复.txt', 'wb') as f:
            f.write(bytes(self.details, encoding='utf-8'))

        print('开始下载!')
        for key in self.url_lst:
            print(f'——————————————————————————————{key}下载中——————————————————————————————')
            page_url = self.url_lst[key]
            text_data = self.single_page_prs(page_url)
            with open(f'C:/Users/AKA阿飞/Desktop/笔趣阁/{self.title}/{key}.txt', 'wb') as f:
                f.write(text_data)

    def main(self, target_url):
        resp_urls = httpx.get(url=target_url, headers=self.headers)
        resp_urls.encoding = 'gbk'
        # print(resp_urls.text)

        print('开始解析网页!')

        html = parsel.Selector(resp_urls.text)

        self.title = html.xpath('//*[@id="info"]/h1//text()').get()
        self.author = html.xpath('//*[@id="info"]/p[1]//text()').get()
        self.details = html.xpath('//*[@id="intro"]/p//text()').get()
        # print(self.title+"\n"+self.author+'\n'+self.details)

        dds = html.xpath('//*[@id="list"]/dl/dd')
        # print(dds)

        print('正在生成url!')

        for dd in dds:
            url = 'https://www.biqooge.com' + dd.xpath('.//a/@href').get()
            title = dd.xpath('.//a//text()').get()
            # print(url + '\n' + title)
            self.url_lst[title] = url

        print('url生成完毕!')
        print('↓'*50)

        self.download()

        # 没有必要的释放
        self.url_lst = {}
        self.title = None
        self.author = None
        self.details = None



if __name__ == "__main__":
    target_url = input('请输入需要下载的小说目录页url:')
    item = Biquge()
    item.main(target_url)


