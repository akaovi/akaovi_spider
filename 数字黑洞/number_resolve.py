class Number_resolve():
    def __init__(self, an_number):
        self.an_number = an_number


    def number_resolve(self):
        list1 = list(str(self.an_number))
        list2 = []
        for i in list1:
            list2.append(int(i))
        return list2
