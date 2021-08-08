# 爬取论坛精选 要求返回作品类型
import os
import re

import parsel
import requests

url = 'http://www.fengniao.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.75'
}
response = requests.get(url=url, headers=headers)
response.encoding = 'GBK'
html = parsel.Selector(response.text)
lis = html.xpath('//*[@id="bbsPart"]/dl/dd/div[1]/ul/li')
for li in lis:
    href = li.xpath('./div/a/@href').get()
    title = li.xpath('./div/div[1]/a/@title').get()
    category = li.xpath('./div/div[2]/a[1]/@title').get()
    pattern = re.compile(u'[\u4e00-\u9fa5]+')
    t_title = re.findall(pattern, title)
    path = 'C:/Users/AKA阿飞/Desktop/蜂鸟网论坛经典/' + t_title[0] + '-' + category + '/'
    print(f'开始下载{title}')
    if os.path.exists(path) == False:
        os.mkdir(path)
    peopleName = li.xpath('./div/div[2]/div/a/@title').get()
    img_html = parsel.Selector(requests.get(url=href, headers=headers).text)
    imgs = img_html.xpath(f'//*[@username="{peopleName}"]')
    i = 0
    for img1 in imgs:
        img_srcs = img1.xpath('./div[@class="aMain"]/div[@class="cont"]/div[@class="img"]')
        for img2 in img_srcs:
            exifBox = img1.xpath('./div[@class="aMain"]/dl[@class="exifBox"]/dd/span//text()').extract()
            if len(exifBox) != 0:
                with open(path + f'{i}.txt', mode='wb') as f1:
                    for k in exifBox:
                        f1.write((k + '\n').encode())
            with open(path + f'{i}.jpg', mode='wb') as f:
                img_src = img2.xpath('./a/img/@src').get()
                img_download = requests.get(url=img_src, headers=headers).content
                f.write(img_download)
                i += 1





