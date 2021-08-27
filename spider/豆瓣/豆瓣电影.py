# -*- coding: utf-8 -*-
# encoding : utf-8
# Author   : aka阿飞
# Datetime : 2021/8/27 22:13
# User     : AKA阿飞
# Product  : PyCharm
# Project  : pycharm
# File     : 豆瓣电影.py

# https://movie.douban.com/
# 示例 https://movie.douban.com/subject/27046740/
# https://movie.douban.com/j/review/13582465/full
import re

import httpx
import parsel


class Doubanmovie:
    def __init__(self):
        self.headers = {
            'Cookie': '',
            'Host': 'movie.douban.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.78'
        }
        self.movie_url = 'https://movie.douban.com/subject/27046740/'

    def parsel_(self):
        print('~~~正在解析网页~~~')
        movie_resp = httpx.get(url=self.movie_url, headers=self.headers)
        movie_html = parsel.Selector(movie_resp.text)
        movie_name = movie_html.xpath('//*[@id="content"]/h1/span[1]/text()').get()
        director = movie_html.xpath('//*[@id="info"]/span[1]/span[2]/a/text()').get()
        Screenwriter = movie_html.xpath('//*[@id="info"]/span[2]/span[2]/a/text()').extract()
        actor = movie_html.xpath('//*[@id="info"]/span[3]/span[2]/a/text()').extract()
        info = '电影:' + movie_name + '\n' + '导演：'+director + '\n' + '编剧：'+','.join(Screenwriter) + '\n' + '主演：'+','.join(actor)
        comment = ''
        comment += '电影简要：'+movie_html.xpath('//*[@id="link-report"]/span/text()').get() + '\n'
        comm = movie_html.xpath('//*[@class="review-list  "]/div/@data-cid').extract()
        for i in comm:
            comment_url = f'https://movie.douban.com/j/review/{i}/full'
            json_data = httpx.get(url=comment_url, headers=self.headers).json()
            comment_ = json_data['html']
            comment += re.sub('<.*?>', '', comment_).replace('&quot;', '').replace('&gt', '') + '\n\n'
        return [movie_name, info + '\n' + comment]

    def download(self, details_lst):
        print('~~~正在保存数据~~~')
        with open(f'./电影{details_lst[0]}的影评.txt', 'wb') as f:
            f.write(bytes(details_lst[1], encoding='utf-8'))

    def run(self):
        detail_lst = self.parsel_()
        self.download(detail_lst)
        print('-->获取完毕-->')


if __name__ == "__main__":
    item = Doubanmovie()
    item.run()

