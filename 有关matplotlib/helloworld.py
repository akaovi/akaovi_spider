import random

import matplotlib.pyplot as plt


class Text():
    def __init__(self):
        pass
    # def run(self):
    #     “”“
    #     函数图像
    #     “”“
    #     xlst = [i for i in range(10)]
    #     ylst = [i**2 for i in range(10)]
    #     plt.plot(xlst, ylst)
    #     plt.tick_params(axis="both", labelsize=14)
    #     plt.show()
    # def run(self):
    #     """
    #     散点图,scatter()
    #     :return:
    #     """
    #     xlst = [i for i in range(10)]
    #     ylst = [i**2 for i in range(10)]
    #     plt.scatter(xlst, ylst)
    #     plt.tick_params(axis='both', labelsize=14)
    #     plt.show()
    def run(self):
        """
        随机漫步
        :return:
        """
        x = 0
        y = 0
        xlst = []
        ylst = []
        n = 0
        while n <= 17:
            x += random.randint(0, 49)
            y += random.randint(0, 49)
            xlst.append(x)
            ylst.append(y)
            n += 1
        plt.scatter(xlst, ylst)
        plt.show()
    # def run(self):
    #     pass
    






item = Text()
item.run()


