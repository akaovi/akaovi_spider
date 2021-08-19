# encoding : utf-8
# Author   : aka阿飞
# Datetime : 2021/8/18 21:57
# User     : AKA阿飞
# Product  : PyCharm
# Project  : pycharm
# File     : 部落.py

# 获得部落的精选、成员数、成员的图片数和粉丝数、部落的影集
# 示例url https://500px.com.cn/page/tribe/detail?tribeId=a6b90b75f02d4344bfb998b7a57541d9
# 部落详情 https://500px.com.cn/community/tribe/tribeDetail?tribeId=a6b90b75f02d4344bfb998b7a57541d9&var=_cur_tribe_detail
# 精选    https://500px.com.cn/community/tribe/listTribeWonderfulGroupPhotosV2?tribeId=a6b90b75f02d4344bfb998b7a57541d9&page=1&size=10&tribeWonderfulGroupId=d0707f559f7244dcb6df8db169d6654e
# 成员    https://500px.com.cn/community/tribe/v3/listUserGroups?page=1&size=20&clientType=web&tribeId=a6b90b75f02d4344bfb998b7a57541d9
# 影集    https://500px.com.cn/community/tribe/getTribeSets?tribeId=a6b90b75f02d4344bfb998b7a57541d9&privacy=1&page=1&size=20&type=json
# 影集之一 https://500px.com.cn/community/set/6330f287db9e4547b31c4c2c2cfaf896/photos?startTime=&page=1&size=20&type=json
import json
import os

import time

import requests


class Buluo:
    def __init__(self, url):
        self.headers = {
            'Cookie': '',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73'
        }
        self.tribeId = url.split('=')[-1]
        self.WonderfulGroupsId = None

    def add_file(self, path):
        """
        检验 path 是否有存在
        有则返回字符串 path
        反之创建并返回字符串 path
        """
        if not os.path.exists(path):
            os.mkdir(path)
        return path

    def img_download_1(self, img_id, uploaderId):
        img_url_1 = f'https://img.500px.me/{img_id}.jpg!p5'
        data = requests.get(url=img_url_1, headers=self.headers).content
        with open(self.add_file(f'C:/Users/AKA阿飞/Desktop/视觉500px/{uploaderId}') + '/' + f'{int(time.time()*100000)}.jpg', 'wb') as f:
            f.write(data)

    def img_dowanload_2(self, img_id, uploaderId):
        img_url = f'https://img.500px.me/photo/{uploaderId}/{img_id}.jpg!p5'
        img_data = requests.get(url=img_url, headers=self.headers).content
        with open(self.add_file(f'C:/Users/AKA阿飞/Desktop/视觉500px/{uploaderId}') + '/' + f'{int(time.time()*100000)}.jpg', 'wb') as f:
            f.write(img_data)


    def tribeDetail(self):
        url = f'https://500px.com.cn/community/tribe/tribeDetail?tribeId={self.tribeId}&var=_cur_tribe_detail'
        json_data = json.loads(requests.get(url=url, headers=self.headers).text[24:])
        WonderfulGroupsId = json.loads(json_data['data']['tribe']['wonderfulGroupsDetail'])[0]['id']
        self.WonderfulGroupsId = WonderfulGroupsId

    def init(self):
        self.tribeDetail()

    def UserGroups(self, page=2):
        print('*' * 20 + '成员' + '*' * 20)
        """
        接数据库使用
        """
        users_lst = []
        for i in range(1, page+1):
            url = f'https://500px.com.cn/community/tribe/v3/listUserGroups?page={i}&size=20&clientType=web&tribeId={self.tribeId}'
            # print(url)
            json_data = requests.get(url=url, headers=self.headers).json()
            for data in json_data['data']:
                user_id = data['id']
                # userName = data['userName']  # 有的没有
                userRole = data['userRole']  # 部落职位
                userUploaderCount = data['userUploaderCount']  # 上传图片数
                userFollowedCount = data['userFollowedCount']  # 粉丝数
                # location = data['location']  # 坐标  有的没有
                tup = (user_id, userRole, userUploaderCount, userFollowedCount)
                users_lst.append(tup)
        print('*' * 20 + '成员' + '*' * 20)
        return tuple(users_lst)

    def jingxuan(self, page=1):
        print('*' * 20 + '精选' + '*' * 20)
        """
        page 默认 --> 1
        """
        for i in range(1, page+1):
            url = f'https://500px.com.cn/community/tribe/listTribeWonderfulGroupPhotosV2?tribeId={self.tribeId}&page={i}&size=10&tribeWonderfulGroupId={self.WonderfulGroupsId}'
            # print(url)
            json_data = requests.get(url=url, headers=self.headers).json()
            # print(json_data)
            for data in json_data['data']:
                img_id = data['id']
                uploaderId = data['uploaderId']
                if img_id[0:5] == '500px':
                    self.img_download_1(img_id, uploaderId)
                    print(f'{img_id}下载完毕!')
                else:
                    self.img_dowanload_2(img_id, uploaderId)
                    print(f'{img_id}下载完毕!')
        print('*'*20 + '精选' + '*'*20)

    def TribeSets(self, page=1):
        print('*' * 20 + '影集' + '*' * 20)
        for i in range(1, page+1):
            TribeSets_url = f'https://500px.com.cn/community/tribe/getTribeSets?tribeId={self.tribeId}&privacy=1&page={i}&size=20&type=json'
            # print(TribeSets_url)
            sets_data = requests.get(url=TribeSets_url, headers=self.headers).json()
            for data in sets_data['data']:
                set_id = data['id']
                # print(set_id)
                title = data['title'].replace(' ', '')
                setSetCount = data['setSetCount']
                # print(setSetCount)
                for k in range(1, int(int(f'{setSetCount}')/20)+2):
                    set_url = f'https://500px.com.cn/community/set/{set_id}/photos?startTime=&page={k}&size=20&type=json'
                    # print(set_url)
                    set_data = requests.get(url=set_url, headers=self.headers).json()
                    for img in set_data['data']:
                        img_id = img['id']
                        # print(img_id)
                        uploaderId = img['uploaderId']
                        if img_id[0:5] == '500px':
                            img_url_1 = f'https://img.500px.me/{img_id}.jpg!p5'
                            data = requests.get(url=img_url_1, headers=self.headers).content
                            with open(self.add_file(
                                    f'C:/Users/AKA阿飞/Desktop/视觉500px/{title}') + '/' + f'{int(time.time() * 100000)}.jpg',
                                      'wb') as f:
                                f.write(data)
                                print(f'{img_id}下载完毕!')
                        else:
                            img_url_2 = f'https://img.500px.me/photo/{uploaderId}/{img_id}.jpg!p5'
                            img_data = requests.get(url=img_url_2, headers=self.headers).content
                            with open(self.add_file(
                                    f'C:/Users/AKA阿飞/Desktop/视觉500px/{title}') + '/' + f'{int(time.time() * 100000)}.jpg',
                                      'wb') as f:
                                f.write(img_data)
                            print(f'{img_id}下载完毕!')
                print(f'{title}下载完毕!')
        print('*' * 20 + '影集' + '*' * 20)

if __name__ == "__main__":
    T_url = 'https://500px.com.cn/page/tribe/detail?tribeId=a6b90b75f02d4344bfb998b7a57541d9'
    item = Buluo(T_url)
    item.init()
    # item.jingxuan()
    # item.UserGroups()
    # item.TribeSets()

