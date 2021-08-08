import random


class Randomwalk():
    def __init__(self):
        pass
    def direct(self):
        d = random.choice([-1, 1])
        return d
    def step(self):
        d = self.direct() * random.choice([1, 2, 3, 4])
        return d
    def run(self, times):
        lst = [0]
        z = 0
        for i in range(times+1):
            z += self.step()
            lst.append(z)
        return lst
