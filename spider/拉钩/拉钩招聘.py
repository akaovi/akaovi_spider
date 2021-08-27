# encoding : utf-8
# Author   : aka阿飞
# Datetime : 2021/8/27 16:59
# User     : AKA阿飞
# Product  : PyCharm
# Project  : pycharm
# File     : 拉钩招聘.py

# url(post) https://www.lagou.com/jobs/v2/positionAjax.json
import re

import httpx


class Lagou:
    def __init__(self):
        self.headers = {
            'cookie': '',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.78'
        }
        self.data = {
            'first': 'true',
            'needAddtionalResult': 'false',
            # 'city': '重庆',  # 就职城市
            'city': input('--->请输入就职城市--->'),
            'px': 'new',
            # 'tagCodeList': 200006,   # python
            # 'gx': '实习',  # 全职 兼职 实习
            'gx': input('--->请输入全职、兼职或实习--->'),
            'fromSearch': 'true',
            # 'kd': '重庆',  # 搜索词
            'kd': input('-->请输入搜索词--->'),
            'pn': 1  # 页码 每页15条招聘信息
        }
        self.job_lst = []
        self.pn_max = int(input('请输入获取的页数: '))

    def parsel_(self):
        while self.data['pn'] <= self.pn_max:
            try:
                json_url = 'https://www.lagou.com/jobs/v2/positionAjax.json'
                json_data = httpx.post(url=json_url, headers=self.headers, data=self.data).json()
                # print(json_data)
                results = json_data['content']['positionResult']['result']
                for position in results:
                    companyLabelList = position['companyLabelList']
                    if not companyLabelList:
                        companyLabelList = '无'
                    else:
                        companyLabelList = ','.join(companyLabelList).strip()
                    positionDetail = position['positionDetail'].replace('&nbsp;', '')
                    positionDetail = re.sub('<.*?>', '', positionDetail)
                    dic = {
                        '公司全称:': position["companyFullName"],
                        '公司地址:': position['district']+'-'+position['positionAddress'],
                        '公司优势:': companyLabelList,
                        '发布时间:': position['createTime'],
                        '学历要求:': position['education'],
                        '职位性质:': position['jobNature'],
                        '职位优势:': position['positionAdvantage'],
                        '职位描述:\n': positionDetail,
                        '职位薪水:': position['salary'],
                    }
                    # print(dic)
                    self.job_lst.append(dic)
                self.data['pn'] += 1
            except:
                self.data['pn'] += 1

    def download(self):
        detail = ''
        with open(f'./位于{self.data["city"]}关于{self.data["kd"]}招聘信息.txt', 'wb') as f:
            for job in self.job_lst:
                for key in job:
                    detail += key+job[key]+'\n'
                detail += '\n\n\n\n'
            f.write(bytes(detail, encoding='utf-8'))

    def run(self):
        self.parsel_()
        self.download()

if __name__ == "__main__":
    item = Lagou()
    item.run()

