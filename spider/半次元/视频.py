# encoding : utf-8
# Author   : aka阿飞
# Datetime : 2021/8/24 17:10
# User     : AKA阿飞
# Product  : PyCharm
# Project  : pycharm
# File     : 视频.py

# https://bcy.net/apiv3/common/getFeeds?refer=channel_video&direction=loadmore&count=12&cid=8103&_signature=BntS5QAAAAAme-x1SeC59wZ7UvAAGdl
# https://bcy.net/item/detail/6934605198098701320?_source_page=video&_sub_channel_name=%E7%83%AD%E9%97%A8
# https://v6-default.ixigua.com/4e642ced45fe1bd1f6a6a5c0c055635a/6124c617/video/tos/cn/tos-cn-v-0064/7b5e774a15e9435daf29578a7d40ab9d/?a=2012&br=1069&bt=1069&cd=0%7C0%7C0&ch=0&cr=0&cs=0&dr=0&ds=4&er=&ft=StTF_hhe663yZF_4kaPb~d5NVgQ&l=202108241711020102120592215C00BC95&lr=&mime_type=video_mp4&net=0&pl=0&qs=9&rc=M3BncHM5MztkMzMzNjQzM0ApOTY6ZTRpOWU1Nzg1aGZmaGc2MGpjZl9haHJgLS1eMTBzczA0NF4xXzMvNmAzLjAuNDM6Yw%3D%3D&vl=&vr=
# https://v6-default.ixigua.com/4e642ced45fe1bd1f6a6a5c0c055635a/6124c617/video/tos/cn/tos-cn-v-0064/7b5e774a15e9435daf29578a7d40ab9d/

# https://ib.365yg.com/video/urls/v/1/toutiao/mp4/v03041g10000c2h6ucukjb13k1i2n78g?r=16047026589127555&s=3483778253&vfrom=xgplayer&_=1629814789979&callback=axiosJsonpCallback1
# https://ib.365yg.com/video/urls/v/1/toutiao/mp4/v03041g10000c2h6ucukjb13k1i2n78g?r=16047026589127555&s=3483778253

import httpx


class Banciyuan:
    def __init__(self):
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.78'
        }
        self.id_lst = []

    def get_id(self):
        print('↓' * 50)
        print('开始获取item_id!')

        json_url = 'https://bcy.net/apiv3/common/getFeeds?refer=channel_video&direction=loadmore&count=12&cid=8103'
        json_data = httpx.get(url=json_url, headers=self.headers).json()
        if json_data['data']['item_info']:
            for ite in json_data['data']['item_info']:
                item_id = ite['item_detail']['item_id']
                self.id_lst.append(item_id)

        print('↓'*50)
        print(self.id_lst)
        print('获取完毕!')

    def run(self):
        """
        每次运行获取12个热门视频
        :return:
        """
        print('↓' * 50)
        print('开始下载视频!')

        ## https://ib.365yg.com/video/urls/v/1/toutiao/mp4/v03041g10000c2h6ucukjb13k1i2n78g?r=16047026589127555&s=3483778253
        # 看不出r和s参数出自哪
        # 得到r和s base64解码获取视频的url

        print('↓' * 50)
        print('视频下载完毕!')


if __name__ == "__main__":
    item = Banciyuan()
    item.run()

