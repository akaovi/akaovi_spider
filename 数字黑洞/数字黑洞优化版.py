from transfor import Transfor
from number_resolve import Number_resolve

def run(an_number):
    a = an_number
    n = 0
    while True:
        if a != 6174:
            numberlist1 = Number_resolve(a)    # 传入参数
            numberlist2 = numberlist1.number_resolve()
            midlenumber = Transfor(numberlist2)
            a = midlenumber.x()
            n += 1
        else:
            break
    print("最终数字是：", a)
    print("执行的次数是：", n)

a = run(8456)
# a = run(6214)
# a = run(1234)
