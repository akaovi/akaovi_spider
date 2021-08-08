# encoding : utf-8
# Author   : aka阿飞
# Datetime : 2021/6/7 22:33
# User     : AKA阿飞
# Product  : PyCharm
# Project  : pycharm
# File     : mihayo.py

# 给定初始id，根据初始id获得json页，获得last_id从而来获取更多图片
import re

import requests

import os

main_url = 'https://bbs.mihoyo.com/dby/home/47?type=2'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.75'
}
path = 'D:/mihoyo数据存储'
class Solution():
    def __init__(self):
        pass

    def req_get(self, last_id):
        json_url = f'https://bbs-api.mihoyo.com/post/wapi/getForumPostList?forum_id=47&gids=5&is_good=false&is_hot=false&last_id={last_id}&page_size=20&sort_type=2'
        json_response = requests.get(url=json_url, headers=headers).json()
        return json_response

    def get_last_id(self, json_response):
        last_id = json_response["data"]["last_id"]
        return last_id

    def img_dit(self, json_response):
        dit = {}
        img_lists = json_response["data"]["list"]
        for img_lst in img_lists:
            img_urls = img_lst["post"]["images"]
            id_name = img_lst["post"]["subject"]
            dit[id_name] = img_urls
        return dit


    def find_chinese(self, file):
        pattern = re.compile(r'[^\w]')
        chinese = re.sub(pattern, '', file)
        return chinese

    def download(self):
        n = 1
        last_id = 6665524
        while True:
            json_response = self.req_get(last_id)
            for key in self.img_dit(json_response).keys():
                print(f'正在为您下在{key}图集!')
                dir_name = self.find_chinese(key)
                if os.path.exists(path+'/'+f'{dir_name}') == False:
                    os.mkdir(path+'/'+f'{dir_name}')
                for value in self.img_dit(json_response)[key]:
                    img = requests.get(url=value, headers=headers).content
                    with open(path+'/'+f'{dir_name}'+f'/{n}.jpg', mode='wb') as f:
                        f.write(img)
                        n += 1
            if n > 200:
                break
            last_id = self.get_last_id(json_response)




item = Solution()
item.download()
