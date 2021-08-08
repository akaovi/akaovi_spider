import os

import parsel
import requests

path = 'C:/Users/AKA阿飞/Desktop/27270爬虫/'

url = 'https://www.27270.net/game/cosplaymeitu/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.75'
}
response = requests.get(url=url, headers=headers)
response.encoding = 'GBK'
html = parsel.Selector(response.text)
lis = html.xpath('/html/body/div[2]/div[1]/div[4]/ul/li')
for li in lis:
    href = li.xpath('.//a/@href').get()
    title = li.xpath('.//a/@title').get()
    path2 = path + title + '/'
    if os.path.exists(path2) == False:
        os.mkdir(path2)
    try:
        for i in range(1, 81):
            with open(path2 + str(i) + '.jpg', mode='wb') as f:
                if i == 1:
                    img_html = parsel.Selector(requests.get(url=href, headers=headers).text)
                    img_url = img_html.xpath('//*[@id="picBody"]/p/a[1]/img/@src').get()
                    img_download = requests.get(url=img_url, headers=headers).content
                    f.write(img_download)
                else:
                    new_href = str(href).replace('.html', f'_{i}.html')
                    img_html = parsel.Selector(requests.get(url=new_href, headers=headers).text)
                    img_url = img_html.xpath('//*[@id="picBody"]/p/a[1]/img/@src').get()
                    img_download = requests.get(url=img_url, headers=headers).content
                    f.write(img_download)
    except:
        continue






