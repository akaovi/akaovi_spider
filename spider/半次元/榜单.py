# encoding : utf-8
# Author   : aka阿飞
# Datetime : 2021/8/19 10:35
# User     : AKA阿飞
# Product  : PyCharm
# Project  : pycharm
# File     : 榜单.py

# 日榜 每天50p
# 周榜 每周150p
# 新人榜 每天最多50p

# 没找sig有的图片无法下载

import base64
import datetime
import os
import time
import httpx
from tqdm import tqdm


class Banciyuan:
    def __init__(self):
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73',
            'cookie': ''
        }
        self.img_url_lst = []

    def add_file(self, path):
        """
        检验 path 是否有存在
        有则返回字符串 path
        反之创建并返回字符串 path
        """
        if not os.path.exists(path):
            os.mkdir(path)
        return path

    def today(self):
        now = datetime.date.today()
        return str(now).replace('-', '')

    def base64_(self, username):
        user_name = f'©{username}\n半次元 - ACG爱好者社区'
        encode = base64.urlsafe_b64encode(user_name.encode())
        return encode

    def get_url(self, sub_type='lastday', date=None, ttype='illust'):
        """
        传入sub_type
        :param sub_type: lastday or week or newPeople
        :param date: 20210824
        :param ttype: illust or cos ps.写作榜没有pa
        :return: None
        """
        if not date:
            u_date = self.today()
        else:
            u_date = date
        for i in range(1, 9):
            lst_url = f'https://bcy.net/apiv3/rank/list/itemInfo?p={i}&ttype={ttype}&sub_type={sub_type}&date={u_date}'
            json_data = httpx.get(url=lst_url, headers=self.headers).json()

            if json_data['data']['top_list_item_info']:
                items = json_data['data']['top_list_item_info']

                for ite in items:
                    uname = ite['item_detail']['uname']
                    uname = f'~tplv-banciyuan-logo-v3:{self.base64_(uname).decode()}.image'
                    image_list = ite['item_detail']['image_list']

                    for img in image_list:
                        img_url = img['path']+uname
                        # print(img_url)
                        self.img_url_lst.append(img_url)

                print('即将获取下一页!')
            else:
                print('已获取全部图片url!')
                break


    def run_day(self, date=None, ttype='illust'):
        """

        :param date:
        :param ttype: illust or cos ps.写作榜没有pa
        :return:
        """
        if not date:
            u_date = self.today()
            self.get_url(ttype=ttype)
        else:
            u_date = date
            self.get_url(u_date, ttype=ttype)

        print('开始下载!')

        for i in tqdm(iterable=range(len(self.img_url_lst)), desc=f"正在下载", unit="张"):
            img_data = httpx.get(url=self.img_url_lst[i], headers=self.headers).content
            with open(self.add_file(f'C:/Users/AKA阿飞/Desktop/半次元/日榜/{u_date}')+'/'+f'{int(time.time()*100000)}.jpg', 'wb') as f:
                f.write(img_data)

        print('下载完毕!')
        self.img_url_lst = []

    def run_week(self, date=None, ttype='illust'):
        """

        :param date:
        :param ttype: illust or cos ps.写作榜没有pa
        :return:
        """
        if not date:
            u_date = self.today()
            self.get_url(sub_type='week', ttype=ttype)
        else:
            u_date = date
            self.get_url(date=u_date, sub_type='week', ttype=ttype)

        print('开始下载!')

        for i in tqdm(iterable=range(len(self.img_url_lst)), desc=f"正在下载", unit="张"):
            img_data = httpx.get(url=self.img_url_lst[i], headers=self.headers).content
            with open(
                    self.add_file(f'C:/Users/AKA阿飞/Desktop/半次元/周榜/{u_date}') + '/' + f'{int(time.time() * 100000)}.jpg',
                    'wb') as f:
                f.write(img_data)

    def run_new(self, date=None, ttype='illust'):
        """

        :param date:
        :param ttype: illust or cos ps.写作榜没有pa
        :return:
        """
        if not date:
            u_date = self.today()
            self.get_url(sub_type='newPeople', ttype=ttype)
        else:
            u_date = date
            self.get_url(date=u_date, sub_type='newPeople', ttype=ttype)

        print('开始下载!')

        for i in tqdm(iterable=range(len(self.img_url_lst)), desc=f"正在下载", unit="张"):
            img_data = httpx.get(url=self.img_url_lst[i], headers=self.headers).content
            with open(
                    self.add_file(f'C:/Users/AKA阿飞/Desktop/半次元/新人榜/{u_date}') + '/' + f'{int(time.time() * 100000)}.jpg',
                    'wb') as f:
                f.write(img_data)


if __name__ == "__main__":
        item = Banciyuan()
        # item.run_day(ttype='cos')
        # item.run_week(ttype='cos')
        # item.run_new(ttype='cos')
