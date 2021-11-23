# -*- coding: utf-8 -*-
# encoding : utf-8
# Author   : aka阿飞
# Datetime : 2021/11/23 0:02
# User     : AKA阿飞
# Product  : PyCharm
# Project  : pycharm
# File     : questionId.py
import time

import httpx


def getQuestionId():

    qestionIdlist = []

    url = "https://creditqa.zhihuishu.com/creditqa/web/qa/getHotQuestionList?uuid=你的uuid&courseId=你的课程id&pageIndex=3&pageSize=50&recruitId=你的reid"
    headers = {"Host": "creditqa.zhihuishu.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 Edg/96.0.1054.29"}
    json_data = httpx.get(url=url, headers=headers).json()

    for info in json_data["rt"]["questionInfoList"]:
        qestionIdlist.append(info["questionId"])

    return qestionIdlist


def getAnswer(qid):
    url = f"https://creditqa.zhihuishu.com/creditqa/web/qa/getAnswerInInfoOrderByTime?uuid=你的uuid&questionId={qid}&sourceType=2&courseId=你的课程id&recruitId=你的reid&pageIndex=0&pageSize=20"
    headers = {"Host": "creditqa.zhihuishu.com",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 Edg/96.0.1054.29"}

    answerinfo = httpx.get(url=url, headers=headers).json()["rt"]["answerInfos"][0]
    answer = answerinfo["answerContent"]
    print("问题为: ", answerinfo["questionContent"])
    print("答案为: ", answer)

    return answer


def saveAnswer(qid, answer):
    headers = {'Cookie': '',
            'Host': 'creditqa.zhihuishu.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 Edg/96.0.1054.29'
    }
    url = "https://creditqa.zhihuishu.com/creditqa/web/qa/saveAnswer"

    postdata = {
        'uuid': '',
        'dateFormate': '',
        'annexs': '[]',
        'qid': f'{qid}',
        'source': '2',
        'aContent': f'{answer}',
        'courseId': '',
        'recruitId': ''
    }

    json_data = httpx.post(url=url, headers=headers, data=postdata).json()
    print(json_data["msg"])


if __name__ == "__main__":
    for i in getQuestionId():
        answer = getAnswer(i)
        saveAnswer(i, answer)
        time.sleep(10)

