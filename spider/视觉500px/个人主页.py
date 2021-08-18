# encoding : utf-8
# Author   : aka阿飞
# Datetime : 2021/8/18 16:11
# User     : AKA阿飞
# Product  : PyCharm
# Project  : pycharm
# File     : 个人主页.py

# 示例 https://500px.com.cn/Stuartphoto
import os

import time

import requests


class Shijue:
    def __init__(self):
        self.headers = {
            'Cookie': 'access_token=6B7E8DE33C6F30B827CC0BF04E1971E5DBB6ACF90C047FA1543562D656BD7832148F0667D881346DC08BEB51FFC39C3DB2C73192FA68E62F82EC2F07ED4F77D3580DE629F6B559A0593E836917C91EA100C233ABE8CFE3D2AAA37DA7AFEBA4EB3972ADD30F3356504E165866BE8B7D0E0B16153564727A6A; token=Token-1b57e9a1-9a74-4b0e-bc05-aa87927fdfca; userId=6a47ba8a84c49aac1bbaeef105b125303; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%226a47ba8a84c49aac1bbaeef105b125303%22%2C%22first_id%22%3A%22178d11cd5714de-010bfacbf6fcd3-71667960-1327104-178d11cd5729e5%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%22178d11cd5714de-010bfacbf6fcd3-71667960-1327104-178d11cd5729e5%22%7D; testapp=s%3ALJT3lXA09H2xmEh2fZ3X5KxGsWSx2xbv.NK0wHZ6xWuOyz9z4CAgT5yQkNp4qzrtJVamJBbYRSIE; acw_tc=2760828016292911135285015eb361f03b9da47855ce821e466b7abe5751e3; SESSION=338ea145-f362-4606-8054-5802df82c84a; Hm_lvt_3eea10d35cb3423b367886fc968de15a=1629099787,1629253882,1629291117; targetUserAvatar=//pic.500px.me/images/default_tx.png; Hm_lpvt_3eea10d35cb3423b367886fc968de15a=1629291140; access_token=6B7E8DE33C6F30B827CC0BF04E1971E5DBB6ACF90C047FA1543562D656BD7832BF04322A0858CF6EC08BEB51FFC39C3DB2C73192FA68E62F82EC2F07ED4F77D3580DE629F6B559A0593E836917C91EA100C233ABE8CFE3D2AAA37DA7AFEBA4EB3972ADD30F3356504E165866BE8B7D0E0B16153564727A6A',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73'
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

    def get_uploaderId(self, one_img_url):
        json_url = f'{one_img_url}?type=json'
        json_data = requests.get(url=json_url, headers=self.headers).json()
        uploaderId = json_data['uploaderId']
        return uploaderId

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

    def main(self, one_img_url, page):
        uploaderId = self.get_uploaderId(one_img_url)
        for i in range(1, page+1):
            try:
                json_url = f'https://500px.com.cn/community/v2/user/profile?resourceType=0,2,4&imgsize=p1,p2,p3&queriedUserId={uploaderId}&startTime=&page={i}&size=20&type=json'
                # print(json_url)
                json_data = requests.get(url=json_url, headers=self.headers).json()
                # print(json_data)
                images = json_data['data']
                # print(images)
                for img in images:
                    img_id = img['id']
                    # print(img_id)
                    if img_id[0:5] == '500px':
                        self.img_download_1(img_id, uploaderId)
                        print(f'{img_id}下载完毕!')
                    else:
                        self.img_dowanload_2(img_id, uploaderId)
                        print(f'{img_id}下载完毕!')
            except:
                return print('*'*10 + 'over!' + '*'*10)


if __name__ == "__main__":
    item = Shijue()
    one_img_url = 'https://500px.com.cn/community/photo-details/84cec3acf39e470aa98ce896112e15c7'
    item.main(one_img_url, 2)
    # 一般情况下，每页20张图片

# 有部分图片下载不成功
