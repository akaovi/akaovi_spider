# -*- coding: utf-8 -*-
# encoding : utf-8
# Author   : aka阿飞
# Datetime : 2021/9/10 20:39
# User     : AKA阿飞
# Product  : PyCharm
# Project  : WeiboAPI
# File     : initial.py


"""
有视频  pageinfo  media_info
图片   pic_infos
作者   screen_name
文本   text_raw
时间   created_at
转发数  reposts_count
评论数  comments_count
点赞数  attitudes_count

"""
import json
import time

import emoji
import httpx
import pymysql


class WeiboAPI:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.headers = {
            'cookie': '',
            'referer': 'https://weibo.com/hot/weibo/102803',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.38',
        }
        self.ram = []

    def mysql_server(self):
        conn = pymysql.connect(
            host="localhost",  # 数据库主机地址
            user="",  # 数据库用户名
            passwd="",  # 数据库密码
            db='weiblog',  # 数据库
            charset='utf8',  # 编码
        )
        # 写入数据
        cur = conn.cursor()
        # 获取插入语句
        for blog in self.ram:
            values = tuple([str(blog[y]) for y in blog])
            print(values)
            js = f"INSERT INTO Blog (author, author_id, text_raw, create_time, share_count, comments_count, nice_count, images, mp4_720p, mp4_hd, mp4_sd) values {values};"
            print(js)
            cur.execute(js)
        # 关闭
        conn.commit()
        cur.close()
        conn.close()
        self.ram = []  # 重置数据

    def parsel_blog(self):
        hot_url = 'https://weibo.com/ajax/feed/hottimeline?since_id=0&refresh=0&group_id=102803&containerid=102803&extparam=discover%7Cnew_feed&max_id=0&count=10'
        resp_rep = httpx.get(url=hot_url, headers=self.headers).text
        json_data = json.loads(resp_rep)
        statuses = json_data['statuses']
        for one in statuses:
            one_blog = {
                'author:': one['user']['screen_name'],
                'author_id:': one['user']['id'],
                'text_raw:': emoji.demojize(one['text_raw'].replace('\u200b', '').replace(' ', '')),
                'create_time:': time.mktime(time.strptime(one['created_at'], '%a %b %d %H:%M:%S %z %Y')),
                'share_count:': one['reposts_count'],
                'comments_count:': one['comments_count'],
                'nice_count:': one['attitudes_count'],
                'images:': [],
                'mp4_720p': 'None',
                'mp4_hd': 'None',
                'mp4_sd': 'None'
            }
            if 'page_info' in one.keys():
                if one['page_info']['object_type'] == 'video':
                    one_blog['mp4_720p'] = one['page_info']['media_info']['mp4_720p_mp4']
                    one_blog['mp4_hd'] = one['page_info']['media_info']['mp4_hd_url']
                    one_blog['mp4_sd'] = one['page_info']['media_info']['mp4_sd_url']
            if 'pic_infos' in one.keys():
                for one_img in one['pic_infos']:
                    one_blog['images:'].append(one['pic_infos'][one_img]['original']['url'])
            self.ram.append(one_blog)
            # print(len(self.ram))
            # print(self.ram)

    def run(self):
        self.parsel_blog()
        self.mysql_server()


if __name__ == '__main__':
    n = 1
    weibo = WeiboAPI()
    while n < 100:
        weibo.run()
        time.sleep(10)
        n += 1
