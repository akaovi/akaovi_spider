import copy
class Transfor():
    def __init__(self, list):
        self.list = list

    def transformax(self):
        nmax = 0
        fakelistm = copy.deepcopy(self.list)
        while True:
            if len(fakelistm) >= 1:
                listmax = max(fakelistm)   # 取出最值
                length = len(fakelistm)
                nmax = nmax + listmax * 10 ** (length - 1)
                fakelistm.remove(listmax)
            else:
                break
        return nmax

    def transformin(self):
        nmin = 0
        fakelistn = copy.deepcopy(self.list)
        while True:
            if len(fakelistn) >= 1:
                listmin = min(fakelistn)
                length = len(fakelistn)
                nmin = nmin + listmin * 10 ** (length - 1)
                fakelistn.remove(listmin)
            else:
                break
        return nmin
    def x(self):
        newnumber = self.transformax() - self.transformin()
        return newnumber
"""
list = [8, 5, 1, 6]
list1 = Transfor(list)
maxlist = list1.transformax()
print(maxlist)
print(list)  # 当成参数传入会改变原有的值
"""
