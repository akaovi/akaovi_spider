# encoding : utf-8
# Author   : aka阿飞
# Datetime : 2021/7/21 18:42
# User     : AKA阿飞
# Product  : PyCharm
# Project  : pycharm
# File     : bilibilidownload.py
import re

import parsel

import requests

import os


def find_chinese(file):
    pattern = re.compile(r'[^\w]')
    chinese = re.sub(pattern, '', file)
    return chinese

if __name__=="__main__":
    url = input('需下载视频的网址: ')

    headers = {
        'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 Edg/91.0.864.71',
        'Referer': 'https://www.bilibili.com/'
    }

    response = requests.get(url=url, headers=headers)
    data_ = response.text
    # print(data_)

    html_ = parsel.Selector(data_)
    # print(html_)

    title_name = html_.xpath('//*[@id="viewbox_report"]/h1/span//text()').get()
    # print(title_name)

    url_list = html_.xpath('/html/head/script[5]//text()').get()
    # print(url_list)

    video_url = re.findall(r'"video":\[{"id":\d+,"baseUrl":"(.*?)"', url_list)[0]
    # print(video_url)

    audio_url = re.findall(r'"audio":\[{"id":\d+,"baseUrl":"(.*?)"', url_list)[0]
    # print(audio_url)


    response_video = requests.get(url=video_url, headers=headers)
    response_audio = requests.get(url=audio_url, headers=headers)

    data_video = response_video.content
    data_audio = response_audio.content

    title_name = find_chinese(title_name)
    # print(title_name)

    with open(f'纯{title_name}.mp4', 'wb') as f:
        f.write(data_video)
    with open(f'纯{title_name}.mp3', 'wb') as f:
        f.write(data_audio)

    os.system(f'ffmpeg -i "纯{title_name}.mp4" -i "纯{title_name}.mp3" -c copy "{title_name}.mp4"')
    os.system(f'del 纯{title_name}.mp4')
    os.system(f'del 纯{title_name}.mp3')


