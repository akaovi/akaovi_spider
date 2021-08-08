import parsel
import requests

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54'
}


def download(url):
    response = requests.get(url=url, headers=headers)
    html = parsel.Selector(response.text)
    lis = html.xpath('//*[@id="anchor_sound_list"]/div[2]/ul/li')
    for li in lis:
        try:
            title = li.xpath('.//a/@title').get()
            id = li.xpath('.//a/@href').get().split('/')[-1]
            print(id)
            json_url = f'https://www.ximalaya.com/revision/play/v1/audio?id={id}&ptype=1'
            json_data = requests.get(url=json_url, headers=headers).json()
            m4a_url = json_data['data']['src']
            down = requests.get(url=m4a_url, headers=headers).content
            with open('音频\\' + title + '.m4a', mode='wb') as f:
                f.write(down)
        except:
            continue


def run():
    url = 'https://www.ximalaya.com/keji/42645914/'
    download(url)
    print('下载完成')

run()
