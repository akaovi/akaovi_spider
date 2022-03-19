
import time

import requests
#
# preUrl = f"https://weiban.mycourse.cn/pharos/usercourse/listCategory.do"
# preData = {
#     'userProjectId': '2b717819-a24f-4f24-b786-bb45746f7348',
#     'chooseType': '3',
#     'userId': '60e6d0d0-5750-4c40-b2ba-1bd55e38b1e5',
#     'tenantCode': '4150010618',
#     'token': 'a0419bc9-e8b1-459c-894c-dfeca0bbe68b',
# }
# headers = {
#     "origin": "https://weiban.mycourse.cn",
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.62",
#     "cookie": "Hm_lvt_a371a0af679e5ae55fe240040f35942e=1642828202,1642828238,1642828287,1642828411; Hm_lpvt_a371a0af679e5ae55fe240040f35942e=1642828411; SERVERID=9ee29c682be9356b7648e0eed94165c1|1642828443|1642825522",
#     "referer": "https://weiban.mycourse.cn",
# }
#
# categoryCodes = requests.post(url=preUrl, headers=headers, data=preData).json()["data"][10:]
#
# for categoryCode in categoryCodes:
#     listCourseUrl = 'https://weiban.mycourse.cn/pharos/usercourse/listCourse.do'
#     listCourseData = {
#         'userProjectId': '007e6e01-f54c-47b2-b848-72149c624c8c',
#         'chooseType': '3',
#         'categoryCode': categoryCode["categoryCode"],
#         'name': '',
#         'userId': '5205bfc6-4e40-49b5-8123-1b2c70eaa14a',
#         'tenantCode': '4150010618',
#         'token': 'd23c1225-9d21-454c-950b-c030442fc863',
#     }
#     listCourseIds = requests.post(url=listCourseUrl, headers=headers, data=listCourseData).json()['data']
#     for listCourseId in listCourseIds:
#         userCourseId = listCourseId['userCourseId']
#
#         # study
#         coursePageUrl = f"https://weiban.mycourse.cn/#/course/detail?courseId=dd85e7a3-d32f-11eb-9a88-d4ae52bad611&userProjectId=007e6e01-f54c-47b2-b848-72149c624c8c&userCourseId={userCourseId}"
#         coursePage = requests.get(url=coursePageUrl, headers=headers)
#
#         studyUrl = 'https://weiban.mycourse.cn/pharos/usercourse/getCourseUrl.do'
#         studyData = {
#             'courseId': 'dd85ea72-d32f-11eb-9a88-d4ae52bad611',
#             'userProjectId': '007e6e01-f54c-47b2-b848-72149c624c8c',
#             'tenantCode': '4150010618',
#             'userId': '5205bfc6-4e40-49b5-8123-1b2c70eaa14a',
#             'token': 'd23c1225-9d21-454c-950b-c030442fc863',
#         }
#         study = requests.get(url=studyUrl, headers=headers, params=studyData)
#         print(study.json())
#         # getCourseIdUrl = 'https://weiban.mycourse.cn/pharos/usercourse/getCourseUrl.do'
#         # getCourseId = requests.post(url=getCourseIdUrl, headers=headers, data=studyData)
#         #
#         # print(getCourseId.json())
#
#         time.sleep(10.1)
#
#         finishUrl = f"https://weiban.mycourse.cn/pharos/usercourse/finish.do?callback=jQuery164027502877770795653_1642827441338&userCourseId={userCourseId}&tenantCode=4150010618"
#
#         finish = requests.get(url=finishUrl, headers=headers)


'''

↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
上面的代码 寒假写的 有问题  懒得删 

'''



"""

1. 登录
2. 大课程学习列表
3. 小学习列表


注意事项：
注意事项：
注意事项：
注意事项：
注意事项：
注意事项：
注意事项：
注意事项：
注意事项：
注意事项：
注意事项：

仅刷课 不考试

需要手动修改所有的userProjectId 、 token 、 userId
需要手动修改所有的userProjectId 、 token 、 userId
需要手动修改所有的userProjectId 、 token 、 userId
需要手动修改所有的userProjectId 、 token 、 userId
需要手动修改所有的userProjectId 、 token 、 userId
需要手动修改所有的userProjectId 、 token 、 userId
需要手动修改所有的userProjectId 、 token 、 userId
需要手动修改所有的userProjectId 、 token 、 userId
需要手动修改所有的userProjectId 、 token 、 userId
需要手动修改所有的userProjectId 、 token 、 userId


其实userProjectId这个可以自动化 但是懒得写了

懒得做自动登录（主要是登录的post里面的编码 我不能解码 不会！ 然后做无头的selenium也懒得做了 就这样了） 主要是懒和不会

↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
猜想：
刷课时间约 118课 * 10s / 60s 大概20min
想节约时间的话 可以用多线程

"""


class Anquanweiban:
    def __init__(self):
        self.headers = {
            'origin': 'http://weiban.mycourse.cn',
            'referer': 'http://weiban.mycourse.cn/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39',
        }

    def login(self):
        pass

    def listCategory(self):
        url = f'https://weiban.mycourse.cn/pharos/usercourse/listCategory.do?timestamp={int(time.time())}'
        data = {
            'userProjectId': '6b225d7e-8cd4-4572-bf47-632e039b85a3',
            'chooseType': '3',
            'userId': '36a81aae-af51-45ab-a353-bf1763d06062',
            'tenantCode': '4150010618',
            'token': 'f174f583-b85e-4963-87f2-57309db056db',
        }
        return requests.post(url=url, headers=self.headers, data=data).json()['data']

    def listCourse(self, categoryCode):
        url = f'https://weiban.mycourse.cn/pharos/usercourse/listCourse.do?timestamp={int(time.time())}'
        data = {
            'userProjectId': '6b225d7e-8cd4-4572-bf47-632e039b85a3',
            'chooseType': '3',
            'categoryCode': f'{categoryCode}',
            'name': '',
            'userId': '36a81aae-af51-45ab-a353-bf1763d06062',
            'tenantCode': '4150010618',
            'token': 'f174f583-b85e-4963-87f2-57309db056db',
        }
        return requests.post(url=url, headers=self.headers, data=data).json()['data']

    def study(self, courseId):
        url = f'https://weiban.mycourse.cn/pharos/usercourse/study.do?timestamp={int(time.time())}'
        data = {
            'courseId': courseId,
            'userProjectId': '6b225d7e-8cd4-4572-bf47-632e039b85a3',
            'tenantCode': '4150010618',
            'userId': '36a81aae-af51-45ab-a353-bf1763d06062',
            'token': 'f174f583-b85e-4963-87f2-57309db056db',
        }
        return requests.post(url=url, headers=self.headers, data=data).json()

    def getCourseUrl(self, courseId):
        url = f'https://weiban.mycourse.cn/pharos/usercourse/getCourseUrl.do?timestamp={int(time.time())}'
        data = {
            'courseId': courseId,
            'userProjectId': '6b225d7e-8cd4-4572-bf47-632e039b85a3',
            'tenantCode': '4150010618',
            'userId': '36a81aae-af51-45ab-a353-bf1763d06062',
            'token': 'f174f583-b85e-4963-87f2-57309db056db',
        }
        return requests.post(url=url, headers=self.headers, data=data).json()

    def finishi(self, i, userCourseId):
        url = f'https://weiban.mycourse.cn/pharos/usercourse/finish.do'
        params = {
            'callback': f'jQuery16402917478197988763_{i}',
            'userCourseId': userCourseId,
            'tenantCode': '4150010618',
            '_': int(time.time()*1000),
        }
        return requests.get(url=url, headers=self.headers, params=params).text


if __name__ == '__main__':
    aqwb = Anquanweiban()
    lc = aqwb.listCategory()
    for cCode in lc:
        categoryCode = cCode['categoryCode']
        totalNum = cCode['totalNum']
        finishedNum = cCode['finishedNum']
        lisccData = aqwb.listCourse(categoryCode)
        for one in range(totalNum - finishedNum):
            userCourseId = lisccData[one]['userCourseId']
            resourceId = lisccData[one]['resourceId']
            print(aqwb.study(resourceId))
            print(aqwb.getCourseUrl(resourceId))
            i = int(time.time() * 1000)
            time.sleep(10)  # 测试之后发现 10s 以下不能完成刷课
            print(aqwb.finishi(i, userCourseId))

