# -*- coding: utf-8 -*-
# encoding : utf-8
# Author   : aka阿飞
# Datetime : 2021/8/28 15:09
# User     : AKA阿飞
# Product  : PyCharm
# Project  : pycharm
# File     : 福彩开奖记录.py

# 获取 双色球--快乐8--福彩3D--七乐彩 的近100期内开奖记录
# http://www.cwl.gov.cn/cwl_admin/kjxx/findDrawNotice?name=ssq&issueCount=100
# http://www.cwl.gov.cn/cwl_admin/kjxx/findDrawNotice?name=kl8&issueCount=100
# http://www.cwl.gov.cn/cwl_admin/kjxx/findDrawNotice?name=3d&issueCount=100
# http://www.cwl.gov.cn/cwl_admin/kjxx/findDrawNotice?name=qlc&issueCount=100

# http://www.cwl.gov.cn/cwl_admin/kjxx/findDrawNotice?name=ssq&issueCount=&issueStart=&issueEnd=&dayStart=2021-01-01&dayEnd=2021-08-28&pageNo=
# http://www.cwl.gov.cn/cwl_admin/kjxx/findDrawNotice?name=kl8&issueCount=&issueStart=&issueEnd=&dayStart=2021-01-01&dayEnd=2021-08-28&pageNo=
# http://www.cwl.gov.cn/cwl_admin/kjxx/findDrawNotice?name=3d&issueCount=&issueStart=&issueEnd=&dayStart=2021-01-01&dayEnd=2021-08-28&pageNo=
# http://www.cwl.gov.cn/cwl_admin/kjxx/findDrawNotice?name=qlc&issueCount=&issueStart=&issueEnd=&dayStart=2021-01-01&dayEnd=2021-08-28&pageNo=
import sys
import xlwt
import httpx


class Fucai:
    def __init__(self):
        self.headers = {
            'Referer': 'http://www.cwl.gov.cn/kjxx/ssq/kjgg/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84'
        }
        self.name = None
        self.result_lst = []

    def asset_name(self):
        name = input('请输入查询彩票名称(双色球--快乐8--福彩3D--七乐彩)：')
        if name == '双色球':
            self.name = 'ssq'
        elif name == '快乐8':
            self.name = 'kl8'
        elif name == '福彩3D':
            self.name = '3d'
        elif name == '七乐彩':
            self.name = 'qlc'
        else:
            sys.exit('输入有误!')

    def main_parsel(self, url):
        response = httpx.get(url=url, headers=self.headers).json()
        results = response['result']
        for result in results:
            blue = result['blue']
            if blue != '':
                blue = ',' + blue
            blue2 = result['blue2']
            if blue2 != '':
                blue2 = ',' + blue2
            dic = {
                '期号：': result['code'],
                '开奖日期：': result['date'],
                '中奖号码：': result['red'] + blue + blue2,
                '总销售额：': result['sales']
            }
            self.result_lst.append(dic)

    def issueCount_parsel(self):
        # count = 100
        count = input('请输入查询期数(最大100期)：')
        resp_url = f'http://www.cwl.gov.cn/cwl_admin/kjxx/findDrawNotice?name={self.name}&issueCount={int(count)}'
        self.main_parsel(resp_url)

    def time_parsel(self):
        dayStart = input('请输入起始日期，形如：2021-01-01-->')
        dayEnd = input('请输入结束日期，形如：2021-01-01-->')
        time_url = f'http://www.cwl.gov.cn/cwl_admin/kjxx/findDrawNotice?name={self.name}&issueCount=&issueStart=&issueEnd=&dayStart={dayStart}&dayEnd={dayEnd}&pageNo='
        self.main_parsel(time_url)
        pageCount = httpx.get(url=time_url, headers=self.headers).json()['pageCount']
        if int(pageCount) > 1:
            for page in range(2, pageCount+1):
                time_url = f'http://www.cwl.gov.cn/cwl_admin/kjxx/findDrawNotice?name={self.name}&issueCount=&issueStart=&issueEnd=&dayStart={dayStart}&dayEnd={dayEnd}&pageNo={page}'
                self.main_parsel(time_url)

    def download(self):
        print('---正在保存数据---')
        book = xlwt.Workbook(encoding='utf-8')
        sheet = book.add_sheet(f'{self.name}', cell_overwrite_ok=True)
        sheet.write(0, 0, '期号')
        sheet.write(0, 1, '开奖日期')
        sheet.write(0, 2, '中奖号码')
        sheet.write(0, 3, '总销售额')
        r = 1
        for dic in self.result_lst:
            c = 0
            row = sheet.row(r)
            for key in dic:
                row.write(c, dic[key])
                c += 1
            r += 1
        book.save(f'{self.name}.xls')

    def run(self):
        self.asset_name()
        type_parsel = input('请输入查询类型：期数--始末日期-->')
        if type_parsel == '期数':
            self.issueCount_parsel()
        elif type_parsel == '始末日期':
            self.time_parsel()
        else:
            sys.exit('输入有误!')
        self.download()
        print('---保存完毕---')


if __name__ == "__main__":
    item = Fucai()
    item.run()

