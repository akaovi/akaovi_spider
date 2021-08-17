# encoding : utf-8
# Author   : aka阿飞
# Datetime : 2021/8/16 20:30
# User     : AKA阿飞
# Product  : PyCharm
# Project  : pycharm
# File     : 主页.py

# https://thomaskksj.tuchong.com/rest/2/sites/395013/posts?count=20&page=2&before_timestamp=1629119853&_signature=_02B4Z6wo00901q49GBwAAIDCLj.iXWj.Iu6uORyAAMqhlsBq6QxhqYE9691FTQh-.7ot8FrM355eT2VmqkUbcQmEy024wNhpXE21Xt5gNZexpEz8WsLkA6FZ064im6BSVQuuZZhW7H2orlerc2
# https://gewala81.tuchong.com/rest/2/sites/2677003/posts?count=20&page=1&before_timestamp=0&_signature=_02B4Z6wo00f012WdXrwAAIDD5Z-k.M.g1VtlmVoAALiIlSA3d.xuT8kFEQUfxlvNRLrNIP.h1ZZirwFo-Bst0Hv-gNDkSOnJO4pGJaA2LLNwMxcmQ9TqO6wWpEWrFTacz.kc5UWTBxIij0P06c
# https://tuchong.com/rest/2/sites/1350538/posts?count=20&page=1&before_timestamp=0&_signature=_02B4Z6wo00f01rGqdkAAAIDCMaiMAyvESh6xrnLAAM19JGQZb7BwrPr0ran0FUh-5MIiaoUQi6uIoE3CylADMXxUbc.gCzy5zM-TWyqtN4WC9G3KBCfVx0mKGIVkYf9ycaY730wvCpGjT4Cd75

# https://thomaskksj.tuchong.com/rest/2/sites/395013/posts?count=20&page=1&before_timestamp=1629119853&_signature=_02B4Z6wo00d014kcoeAAAIDDCR5boOWXIf-JGKVAAINlKDUzbItoj2BUP-k68iUZ6f-7tzgWD7tL3bwmc6Z5PxOun3KJ57y47H2oGcvBM3WxdstN4AwArhskWRe626hUT0KCZajKfQ3gDGvZd8
# https://gewala81.tuchong.com/rest/2/sites/2677003/posts?count=20&page=2&before_timestamp=1629120423&_signature=_02B4Z6wo00d01.kfPIwAAIDDeR3Gzseq9K.5GzgAAJ9nOsXQTPuKsHkEKvqdqgvPxyYixnC.q58fBdsOY4TI.ovJ8mJ8FYJBzF90msMWOtcFoH0qzng0aPTa.HVbm.T3JS4yBea66CUrmFlT06
# https://tuchong.com/rest/2/sites/1350538/posts?count=20&page=2&before_timestamp=1629120573&_signature=_02B4Z6wo00d01yhSR5wAAIDDqFC93ddnda8oVkMAAKsZBRG3.PQh.CuLzRat8GVu9ZK945EteCmRsJB3PN7uVYTGB.xP7uf2jgTAaw9wHDRNa8jU-rMqLuoam.8hajbFM-tKaC-rl413R4wh28

# https://thomaskksj.tuchong.com/rest/2/sites/395013/posts?count=20&page=1
# https://gewala81.tuchong.com/rest/2/sites/2677003/posts?count=20&page=1
# https://tuchong.com/rest/2/sites/1350538/posts?count=20&page=1
# https://{前缀}/rest/2/sites/{id}/posts?count=20&page={}

# https://thomaskksj.tuchong.com/rest/2/users/395013/favorites?count=20&page=1&before_timestamp=&_signature=_02B4Z6wo00d01jiGA0AAAIDCuIT5AhAE.Uo4ggfAAO9K3HOKlMMJm7a-XVoDrtFszBudqB3RmUapGDxOh5QxMnkLRMNDZgJx.8u8TGhUF8N-4au4Zrr9y6bNGm6xFhCiuzGhU9GQzXkPTSTs79
# https://thomaskksj.tuchong.com/rest/2/sites/395013/posts?count=20&page=2&before_timestamp=1629119853&_signature=_02B4Z6wo00901q49GBwAAIDCLj.iXWj.Iu6uORyAAMqhlsBq6QxhqYE9691FTQh-.7ot8FrM355eT2VmqkUbcQmEy024wNhpXE21Xt5gNZexpEz8WsLkA6FZ064im6BSVQuuZZhW7H2orlerc2
import base64
import json
import os

import time

import requests


class Tuchong:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67',
            'cookie': 'wluuid=WLGEUST-9B11240F-82EC-AF82-B088-931C9810FAD4; ssoflag=0; wlsource=tc_pc_home_search; __utmz=115147160.1618918335.4.2.utmcsr=tuchong.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _ga=GA1.2.694931593.1618413531; lang=zh; creative_device_id=fc4cbd43-caf8-4970-843f-55250e6c33f9; creative_token=eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2MjkwOTk5NzYsInZhbCI6IkZWSzdJU0JKUE9PV0ZGRFVaSlVSM0FPVzcyT0pUQ0I2QTQ0VVFVQ0xJNE1LSDVaRkZZRVEifQ.q2gpR7OtZ_bGqabwLDYlJbJToKwwxYL6JNefNNqemkFBwRvSvmbqwY1GYZzsT9Ao; token=f54c79b50f97afdd; __utma=115147160.694931593.1618413531.1622365801.1629101618.6; MONITOR_WEB_ID=24894185; webp_enabled=1; source=tc_pc_pic_download; PHPSESSID=m0hkca3bkmtun4vql5km4b83hc; ttcid=fac82b5a151d4f9eaf52bdd569c02dc535; log_web_id=5436512731; MONITOR_WEB_ID=24894185; tt_scid=udyh-mZvroNeVhD1Jlg-uI5GvJLK53zYVF0pm4OPd9HhxggrtBSlbVVtPvjdcCOw953b'
        }
        # cookie 过期

    def add_file(self, path):
        """
        检验 path 是否有存在
        有则返回字符串 path
        反之创建并返回字符串 path
        """
        if not os.path.exists(path):
            os.mkdir(path)
        return path

    def url_filter(self, one_img_url):
        """
        通过形如： https://thomaskksj.tuchong.com/100804773/ 作者的一张图片的url
        得到形如： https://{thomaskksj.tuchong.com}/rest/2/sites/{}/posts?count=20&page={}

        https://thomaskksj.tuchong.com/23593519/#image20030715
        https://thomaskksj.tuchong.com/23593519/
        https://thomaskksj.tuchong.com/rest/posts/38759241
        """
        img_id = one_img_url.split('/')[-2]
        first = one_img_url.split('/')[2]

        url = one_img_url.replace(f'{img_id}/', f'rest/posts/{img_id}')
        json_data = requests.get(url=url, headers=self.headers).json()
        author_id = json_data['post']['author_id']
        return first, author_id

    def download(self, url, author_id, post_id):
        """
        """
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67',
        }
        data = requests.get(url=url, headers=headers).content
        with open(self.add_file(f'C:/Users/AKA阿飞/Desktop/图虫/{author_id}/{post_id}') + '/' + f'{int(time.time() * 1000000)}.jpg', 'wb') as f:
            f.write(data)

    def video_download(self, video_url, author_id, video_id):
        data = requests.get(url=video_url, headers=self.headers).content
        with open(self.add_file(
                f'C:/Users/AKA阿飞/Desktop/图虫/{author_id}/{video_id}') + '/' + f'{int(time.time() * 1000000)}.mp4',
                  'wb') as f:
            f.write(data)

    def main(self, position: str, one_img_url, page: int):
        """
        position:
            图文 --> posts
            喜欢 --> favorites
            视频 --> videos
        one_img_url 作者的一张图片
        page 下载的页数
        true , null, false 变为字符串
        """
        true = "true"
        false = "false"
        null = "null"
        if type(page) == int:
            first, author_id = self.url_filter(one_img_url)
            self.add_file(f'C:/Users/AKA阿飞/Desktop/图虫/{author_id}')
            for i in range(1, page+1):
                if position == 'videos':
                    req_url = f'https://{first}/rest/users/{author_id}/{position}?count=20&page={i}'
                    json_data = requests.get(url=req_url, headers=self.headers).json()
                    # print(json_data)
                    videoList = json_data['videoList']
                    # print(videoList)
                    for video in videoList:
                        video_id = video['video_id']
                        # print(json.loads(video['video_model']))
                        video_list = json.loads(video['video_model'])['video_list']
                        # print(video_list)
                        if 'video_5' in video_list:
                            video_url = str(base64.b64decode(video_list['video_5']['main_url']), "utf-8")
                            self.video_download(video_url, author_id, video_id)
                            print(f'{video_id}下载完毕!')
                        elif 'video_4' in video_list:
                            video_url = str(base64.b64decode(video_list['video_4']['main_url']), "utf-8")
                            self.video_download(video_url, author_id, video_id)
                            print(f'{video_id}下载完毕!')
                        elif 'video_3' in video_list:
                            video_url = str(base64.b64decode(video_list['video_3']['main_url']), "utf-8")
                            self.video_download(video_url, author_id, video_id)
                            print(f'{video_id}下载完毕!')
                        else:
                            video_url = str(base64.b64decode(video_list['video_2']['main_url']), "utf-8")
                            self.video_download(video_url, author_id, video_id)
                            print(f'{video_id}下载完毕!')
                else:
                    if position == 'posts':
                        req_url = f'https://{first}/rest/2/sites/{author_id}/{position}?count=20&page={i}'
                    else:
                        req_url = f'https://{first}/rest/2/users/{author_id}/{position}?count=20&page={i}'
                    json_data = requests.get(url=req_url, headers=self.headers).json()
                    post_list = json_data['post_list']
                    for work in post_list:
                        post_id = work['post_id']
                        images = work['images']
                        for img in images:
                            img_url = img['source']['f']
                            self.download(img_url, author_id, post_id)
                        print('*'*10 + str(post_id) + '下载完毕' + '*'*10)
        else:
            print('请输入整数页!')




if __name__ == "__main__":
    url = 'https://xiaoyaimage.tuchong.com/31913051/'
    item = Tuchong()
    item.main('videos', url, 2)
    # 测试第2页跟第1页一模一样

