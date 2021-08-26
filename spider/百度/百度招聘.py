# encoding : utf-8
# Author   : aka阿飞
# Datetime : 2021/8/25 23:36
# User     : AKA阿飞
# Product  : PyCharm
# Project  : pycharm
# File     : 百度招聘.py

# https://zhaopin.baidu.com/quanzhi?query=爬虫city=

import json
import re
import time
import parsel
from selenium import webdriver


class Baiduzhaopin:
    def __init__(self):
        self.username = input('请输入你的百度账号:')
        self.password = input('请输入你的密码:')
        self.query = input('请输入招聘岗位名称')
        self.city = input('请输入工作城市:')
        self.url = f'https://zhaopin.baidu.com/quanzhi?query={self.query}&city={self.city}'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.78'
        }
        self.driver = webdriver.Edge('F:/下载/msedgedriver.exe')
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.per_url = []
        self.dic_lst = []

    def lst_resolve(self, lst):
        result = [x.replace('\n', '').replace(' ', '') for x in lst if x != '']
        result = [x for x in result if x != '']
        result = '  '.join(result)
        return result

    def login(self):
        self.driver.find_element_by_xpath('//*[@class="tang-pass-footerBarULogin pass-link"]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@class="pass-text-input pass-text-input-userName"]').send_keys(
            self.username)
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@class="pass-text-input pass-text-input-password"]').send_keys(
            self.password)
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_3__submit"]').click()

    def single_page_parsel(self):
        self.driver.get(self.url)
        time.sleep(1)
        self.login()
        time.sleep(7)
        self.driver.execute_script('window.scrollTo(0,10000)')
        time.sleep(2)
        self.driver.execute_script('window.scrollTo(0,10000)')
        time.sleep(2)
        resp = self.driver.page_source
        # print(resp)
        result = re.findall('data\["list"] = \[.*?];', resp)
        result = result[0].replace('data["list"] = ', '')
        result = result[:-1]
        # print(result)
        return json.loads(result)

    def save(self, dic):
        print('~~~~~~~~保存数据ing~~~~~~~~')
        comm = ''
        with open(f'./{self.query}招聘信息.txt', 'wb') as f:
            for i in dic:
                for key in i:
                    data = key + i[key] + '\n'
                    comm += data
                comm += '\n\n'
            f.write(bytes(comm, encoding='utf-8'))

    def run(self):
        json_data = self.single_page_parsel()
        for per_page in json_data:
            loc = per_page['loc']
            self.per_url.append(loc)
        print('已完成url处理，开始获取文本!')
        for url in self.per_url:

            # 指定爬取数目
            if self.per_url.index(url) + 1 > 15:
                break

            # print(url)
            page_url = f'https://zhaopin.baidu.com/szzw?id={url}&query={self.query}&city={self.city}&is_promise=1&is_direct=&vip_sign=&asp_ad_job='
            time.sleep(1)
            self.driver.get(page_url)
            time.sleep(5)
            resp = self.driver.page_source
            html = parsel.Selector(resp)

            job_name = html.xpath('//*[@id="main"]/div[1]/h4/text()').get()
            # print(job_name)

            if html.xpath('//*[@id="main"]/div[1]/div[2]/div[1]/span[2]/text()').get() == None:
                salary = html.xpath('//*[@id="main"]/div[1]/div[2]/div[1]/span[1]/text()').get()
            else:
                salary = html.xpath('//*[@id="main"]/div[1]/div[2]/div[1]/span[1]/text()').get() + html.xpath('//*[@id="main"]/div[1]/div[2]/div[1]/span[2]/text()').get()
            # print(salary)

            job_require = html.xpath('//*[@id="main"]/div[1]/div[3]//text()').get() + html.xpath('//*[@id="main"]/div[1]/div[3]/text()[2]').get() + html.xpath('//*[@id="main"]/div[1]/div[3]/span/text()').get()
            if job_require == None:
                company_welfare = '未写需求'
            # print(job_require)

            company_welfare = html.xpath('//*[@id="main"]/div[3]/div[1]/div[1]/div[2]/p/span//text()').get()
            if company_welfare == None:
                company_welfare = '无公司福利'
            # print(company_welfare)

            job_classfiy = html.xpath('//*[@id="main"]/div[3]/div[1]/div[1]/div[3]/p//text()').extract()
            # print(job_classfiy)

            job_classfiy = self.lst_resolve(job_classfiy)
            # print(job_classfiy)

            job_description = html.xpath('//*[@id="main"]/div[3]/div[1]/div[1]/div[4]/div/p//text()').get()
            if job_description == None:
                job_description = '未写详细描述'
            # print(job_description)

            job_addr = html.xpath('//*[@id="main"]/div[3]/div[1]/div[1]/div[5]/p[1]/text()').get() + html.xpath('//*[@id="main"]/div[3]/div[1]/div[1]/div[5]/p[2]/text()').get()
            if job_addr == None:
                job_addr = '未写工作地址'
            # print(job_addr)

            dic = {
                '工作全称:': job_name,
                '月薪:': salary,
                '工作需求:': job_require,
                '公司福利:': company_welfare,
                '工作类型:': job_classfiy,
                '工作内容:': job_description,
                '工作地址:': job_addr
            }
            # print(dic)
            self.dic_lst.append(dic)
        self.save(self.dic_lst)
        self.driver.quit()
        print('---程序结束运行---')


if __name__ == "__main__":
    item = Baiduzhaopin()
    item.run()
