import csv

header = ['word', 'num']
f = open('F:/下载/2018年年12月大学英语四级真题完整版(第2套).doc - 百度文库.txt', encoding='utf-8')
with open('./wen.txt', mode='wb') as k:
    for i in f.read():
        if i.isalpha() == True:
            k.write(i.encode().lower())
        else:
            k.write(','.encode())

f.close()

a = open('./wen.txt', encoding='utf-8')
st = a.read().split(',')
word = {}
for i in st:
    if i.isalpha() == True:
        if word.__contains__(i) == True:
            word[i] += 1
        else:
            word[i] = 1

print(word)
with open('./sort.csv', 'a', newline='', encoding='utf-8') as l:
    writer = csv.DictWriter(l, fieldnames=header)
    writer.writeheader()
    for w in word:
        datas = [{'word': w, 'num': word[w]}]
        writer.writerows(datas)

a.close()



