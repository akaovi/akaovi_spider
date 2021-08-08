import re
import requests
from lxml import etree
import datetime
import time

# 设置保存路径
path = '图片\\'
# 目标url
url = "http://pic.netbian.com/4kmeinv/index.html"
# 伪装请求头  防止被反爬
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.44",
    "Referer": "http://pic.netbian.com/4kmeinv/index.html"
}

start = datetime.datetime.now()

def get_img(urls):
    for url in urls:
        # 发送请求  获取响应
        response = requests.get(url, headers=headers)
        # 打印网页源代码来看  乱码   重新设置编码解决编码问题
        # 内容正常显示  便于之后提取数据
        response.encoding = 'GBK'
        html = etree.HTML(response.text)
        # xpath定位提取想要的数据  得到图片链接和名称
        img_src = html.xpath('//ul[@class="clearfix"]/li/a/img/@src')
        # 列表推导式   得到真正的图片url
        img_src = ['http://pic.netbian.com' + x for x in img_src]
        img_alt = html.xpath('//ul[@class="clearfix"]/li/a/img/@alt')
        for src, name in zip(img_src, img_alt):
            img_content = requests.get(src, headers=headers).content
            img_name = name + '.jpg'
            with open(path + img_name, 'wb') as f:  # 图片保存到本地
                # print(f"正在为您下载图片：{img_name}")
                f.write(img_content)
        time.sleep(1)

def main():
    # 要请求的url列表
    url_list = ['http://pic.netbian.com/4kmeinv/index.html'] + [f'http://pic.netbian.com/4kmeinv/index_{i}.html' for i in range(2, 11)]
    get_img(url_list)
    delta = (datetime.datetime.now() - start).total_seconds()
    print(f"抓取10页图片用时：{delta}s")


if __name__ == '__main__':
    main()
