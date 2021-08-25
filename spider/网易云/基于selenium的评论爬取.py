# encoding : utf-8
# Author   : aka阿飞
# Datetime : 2021/8/10 15:55
# User     : AKA阿飞
# Product  : PyCharm
# Project  : pycharm
# File     : hot_comments.py


# 基于selenium  懒得做js解密
import parsel
from selenium import webdriver


class Wangyiyun:
    def __init__(self):
        # 全部都是你
        # self.url = 'https://music.163.com/#/song?id={}'.format()
        # self.url = 'https://music.163.com/#/song?id=1383954630'
        self.page = 2
        self.comment = ''
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67'
        }
        self.driver = webdriver.Edge('F:/下载/msedgedriver.exe')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def single_page(self, target_url):
        self.driver.get(target_url)
        self.driver.switch_to_frame('contentFrame')
        self.driver.execute_script("window.scrollTo(0,5000);")
        for page in range(self.page):
            resp = self.driver.page_source
            html = parsel.Selector(resp)
            # print(html)
            comments = html.xpath('//*[@class="cmmts j-flag"]/div')
            for com in comments:
                username = com.xpath('.//a[@class="s-fc7"]/text()').get()
                comment = com.xpath('.//div[@class="cnt f-brk"]/text()').get()
                if comment == None:
                    comment = ''
                else:
                    comment = comment[1:]
                comment_time = com.xpath('.//div[@class="time s-fc4"]/text()').get()
                comment_like = com.xpath('.//a[@data-type="like"]/text()').get()
                if comment_like == None:
                    comment_like = '0'
                self.comment += '用户:'+str(username) + '\n' + str(comment) + '\n' + str(comment_like) + '\n' + str(comment_time) + '\n\n'
            self.driver.find_elements_by_xpath('/html/body/div[3]/div[1]/div/div/div[2]/div/div[2]/div[3]/div/a[@href="#"]')[-1].click()
        self.driver.quit()

    def run(self, target_url):
        self.single_page(target_url)
        print(self.comment)


if __name__ == '__main__':
    target_url = input('请输入目标网址:')
    item = Wangyiyun()
    item.run(target_url)
