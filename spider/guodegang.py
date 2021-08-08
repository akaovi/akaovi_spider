"""郭德纲相声下载项目练手"""

import parsel
import requests


headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54'
    }

def download(url):
    # 请求网页
    response = requests.get(url=url, headers=headers)
    # 解析网址获取标签内容
    html = parsel.Selector(response.text)

    lis = html.xpath('//*[@id="anchor_sound_list"]/div[2]/ul/li')

    for li in lis:
        # 获取下载标题
        title = li.xpath('.//a/@title').get()
        print('正在下载', title)
        # 获取音频对应数据包的id
        id = li.xpath('.//a/@href').get().split('/')[-1]
        # 获取数据包的信息
        json_url = f'https://www.ximalaya.com/revision/play/v1/audio?id={id}&ptype=1'
        json_date = requests.get(url=json_url, headers=headers).json()
        # 获取数据包中的音频下载地址
        m4a_url = json_date['data']['src']
        m4a_content = requests.get(url=m4a_url, headers=headers).content
        # 音频写入文件
        with open('video\\' + title + '.m4a', mode='wb') as f:
            f.write(m4a_content)

def run():
    for i in range(1, 6):
        url = f'https://www.ximalaya.com/xiangsheng/9723091/p{i}/'
        download(url)
        print(f"=============================第{i}页下载完成=============================")

run()
