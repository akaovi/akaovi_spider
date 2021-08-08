import datetime
import os

import parsel
import requests


def titlename():
    """
    获取上一天时间作为文件名
    """
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    datetoday = str(yesterday).split('-')
    date = ''
    for i in datetoday:
        date += i
    return date

name = titlename()

path = r'C:\Users\AKA阿飞\Desktop\china daily top3' + '/' + name + '/'

url = 'http://www.chinadaily.com.cn/opinion/topdiscusstion'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36 Edg/89.0.774.77'
}

response = requests.get(url=url, headers=headers)
html = parsel.Selector(response.text)
href1 = 'http:' + html.xpath('//*[@id="left"]/div[1]/span[2]/h4/a/@href').get()
href2 = 'http:' + html.xpath('//*[@id="left"]/div[2]/span[2]/h4/a/@href').get()
href3 = 'http:' + html.xpath('//*[@id="left"]/div[3]/span[2]/h4/a/@href').get()

for href in href1, href2, href3:
    text = requests.get(url=href, headers=headers)
    html_text = parsel.Selector(text.text)
    title = html_text.xpath('//*[@id="lft-art"]/h1//text()').get()
    ps = html_text.xpath('//*[@id="Content"]/p')
    if os.path.exists(path) == False:
        os.mkdir(path)
    with open(path + title + '.txt', mode='wb') as f:
        for p in ps:
            text_text = p.xpath('.//text()').get()
            f.write(text_text.encode())






