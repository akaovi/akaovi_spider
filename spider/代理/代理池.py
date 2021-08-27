# encoding : utf-8
# Author   : aka阿飞
# Datetime : 2021/8/27 10:12
# User     : AKA阿飞
# Product  : PyCharm
# Project  : pycharm
# File     : proxy_ip.py

# 构建代理ip池

import random
import re
import parsel
import requests


class Proxy:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.78'
        }
        self.getnum = '10'

    def anxiaomo(self):
        print('---请稍后---')
        print('---正在生成http代理---')
        print('---喝杯茶取吧---')
        proxy_lst = []
        anxiaomo_url = 'http://www.66ip.cn/areaindex_4/1.html'
        resp = requests.get(url=anxiaomo_url, headers=self.headers)
        resp.encoding = 'gbk'
        tr_lst = re.findall('<tr>.*?</tr>', resp.text)
        for tr in tr_lst:
            if not re.findall('<td>\d+\.\d+\.\d+\.\d+</td>', tr):
                continue
            ip = re.findall('<td>\d+\.\d+\.\d+\.\d+</td>', tr)[0].replace('<td>', '').replace('</td>', '')
            port = re.findall('<td>\d+</td>', tr)[0].replace('<td>', '').replace('</td>', '')
            dic = {
                'https': f'https://{ip}:{port}',
            }
            # print(dic)
            baidu = 'http://gate.baidu.com/'
            try:
                r = requests.get(url=baidu, headers=self.headers, proxies=dic, timeout=5)
                if r.status_code == 200:
                    proxy_lst.append(dic)
            except:
                continue
        return proxy_lst

    def ip_89(self):
        print('---请稍后---')
        print('---正在生成http代理---')
        print('---喝杯茶取吧---')
        proxy_lst = []
        for page in range(1, 3):
            ip_89_url = f'https://www.89ip.cn/index_{page}.html'
            response = requests.get(url=ip_89_url, headers=self.headers)
            html = parsel.Selector(response.text)
            tr_lst = html.xpath('//table[@class="layui-table"]/tbody/tr')
            for tr in tr_lst:
                ip = tr.xpath("./td[1]/text()").get().replace('\n', '').replace('\t', '').replace('\r', '')
                port = tr.xpath("./td[2]/text()").get().replace('\n', '').replace('\t', '').replace('\r', '')
                dic = {
                    'https': f'https://{ip}:{port}',
                }
                baidu = 'http://gate.baidu.com/'
                try:
                    r = requests.get(url=baidu, headers=self.headers, proxies=dic, timeout=5)
                    if r.status_code == 200:
                        proxy_lst.append(dic)
                except:
                    continue
        return proxy_lst

    def yundaili(self):
        print('---请稍后---')
        print('---正在生成http代理---')
        print('---喝杯茶取吧---')
        proxy_lst = []
        for page in range(1, 4):
            yundaili_url = 'http://www.ip3366.net/?stype=1&page=1'
            response = requests.get(url=yundaili_url, headers=self.headers)
            html = parsel.Selector(response.text)
            tr_lst = html.xpath('//*[@id="list"]/table/tbody/tr')
            for tr in tr_lst:
                ip = tr.xpath('./td[1]/text()').get()
                port = tr.xpath('./td[2]/text()').get()
                dic = {
                    'https': f'https://{ip}:{port}'
                }
                # print(dic)
                baidu = 'http://gate.baidu.com/'
                try:
                    r = requests.get(url=baidu, headers=self.headers, proxies=dic, timeout=5)
                    # print(r.status_code)
                    if r.status_code == 200:
                        proxy_lst.append(dic)
                except:
                    continue
        return proxy_lst

    def kauidaili(self):
        print('---请稍后---')
        print('---正在生成http代理---')
        print('---喝杯茶取吧---')
        proxy_lst = []
        for page in range(1, 4):
            kuaidaili_url = f'https://www.kuaidaili.com/free/inha/{page}/'
            response = requests.get(url=kuaidaili_url, headers=self.headers)
            html = parsel.Selector(response.text)
            tr_lst = html.xpath('//*[@id="list"]/table/tbody/tr')
            for tr in tr_lst:
                ip = tr.xpath('./td[1]/text()').get()
                port = tr.xpath('./td[2]/text()').get()
                dic = {
                    'https': f'https://{ip}:{port}'
                }
                # print(dic)
                baidu = 'http://gate.baidu.com/'
                try:
                    r = requests.get(url=baidu, headers=self.headers, proxies=dic, timeout=5)
                    # print(r.status_code)
                    if r.status_code == 200:
                        proxy_lst.append(dic)
                except:
                    continue
        return proxy_lst

    def xila(self):
        print('---请稍后---')
        print('---正在生成http代理---')
        print('---喝杯茶取吧---')
        proxy_lst = []
        for page in range(1, 3):
            xila_url = f'http://www.xiladaili.com/gaoni/{page}/'
            response = requests.get(url=xila_url, headers=self.headers)
            html = parsel.Selector(response.text)
            tr_lst = html.xpath('//table[@class="fl-table"]/tbody/tr')
            for tr in tr_lst:
                ip_port = tr.xpath('./td[1]/text()').get()
                dic = {
                    'https': f'https://{ip_port}'
                }
                print(dic)
                baidu = 'http://gate.baidu.com/'
                try:
                    r = requests.get(url=baidu, headers=self.headers, proxies=dic, timeout=5)
                    print(r.status_code)
                    if r.status_code == 200:
                        proxy_lst.append(dic)
                except:
                    continue
        return proxy_lst

    def xiaohuan(self):
        print('---请稍后---')
        print('---正在生成http代理---')
        print('---喝杯茶取吧---')
        proxy_lst = []
        xiaohuan_url = 'https://ip.ihuan.me/'
        response = requests.get(url=xiaohuan_url, headers=self.headers)
        html = parsel.Selector(response.text)
        tr_lst = html.xpath('//table[@class="table table-hover table-bordered"]/tbody/tr')
        for tr in tr_lst:
            ip = tr.xpath('./td[1]/a/text()').get()
            port = tr.xpath('./td[2]/text()').get()
            dic = {
                'https': f'https://{ip}:{port}'
            }
            # print(dic)
            baidu = 'http://gate.baidu.com/'
            try:
                r = requests.get(url=baidu, headers=self.headers, proxies=dic, timeout=5)
                # print(r.status_code)
                if r.status_code == 200:
                    proxy_lst.append(dic)
            except:
                continue
        return proxy_lst

    def run(self):
        random_num = random.randint(1, 6)
        if random_num == 1:
            lst = self.anxiaomo()
        elif random_num == 2:
            lst = self.ip_89()
        elif random_num == 3:
            lst = self.yundaili()
        elif random_num == 4:
            lst = self.kauidaili()
        elif random_num == 5:
            lst = self.xila()
        else:
            lst = self.xiaohuan()
        print(lst)
        return lst


if __name__ == "__main__":
    item = Proxy()
    item.run()

