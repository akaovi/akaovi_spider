import csv


class Text_processing():
    header = ['word', 'num']
    word = {}

    def __init__(self):
        pass
    def pretreat(self, path):
        f = open(path, encoding='utf-8')
        with open('./wen.txt', mode='wb') as k:
            for i in f.read():
                if i.isalpha() == True:
                    k.write(i.encode().lower())
                else:
                    k.write(','.encode())
        f.close()
    def storage(self):
        with open('./sort.csv', 'a', newline='', encoding='utf-8') as l:
            writer = csv.DictWriter(l, fieldnames=self.header)
            writer.writeheader()
            for w in self.word:
                datas = [{'word': w, 'num': self.word[w]}]
                writer.writerows(datas)
    def statistic(self):
        a = open('./wen.txt', encoding='utf-8')
        st = a.read().split(',')
        for i in st:
            if i.isalpha() == True:
                if self.word.__contains__(i) == True:
                    self.word[i] += 1
                else:
                    self.word[i] = 1
        a.close()
    def run(self, path):
        pass

paths = ['F:/下载/2018年年12月大学英语四级真题完整版(第2套).doc - 百度文库.txt', 'F:/下载/2019年12月四级真题三套(全) - 百度文库.txt', 'F:/下载/2019年大学英语四级真题试卷及答案 - 百度文库.txt', 'F:/下载/2020年12月英语四级真题及参考答案-三套全 - 百度文库.txt', 'F:/下载/2020年精品-大学英语四级真题及答案 - 百度文库.txt']
item = Text_processing()
for i in paths:
    item.pretreat(i)
    item.statistic()
    print(item.word)
item.storage()
