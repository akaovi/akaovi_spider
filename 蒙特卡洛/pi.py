import random
import datetime

# 随机落点
def r_location():
    x,y = (random.uniform(0, 1), random.uniform(0, 1))
    return x,y

# 落点位置与计算
def run(simulation_times):
    start = datetime.datetime.now()
    n = 0
    n_s = 0
    n_c = 0
    while True:
        if n <= simulation_times:
            n += 1
            x,y = r_location()
            if x**2 + y**2 <= 1:
                n_s += 1
                n_c += 1
            else:
                n_s += 1
        else:
            break
    reslut = 4 * (n_c / n_s)
    delta = (datetime.datetime.now() - start).total_seconds()
    return print("Π的大小是：", reslut), print("计算用时为：", delta)

run(10000)
# 跑1亿次要146s，慎重
