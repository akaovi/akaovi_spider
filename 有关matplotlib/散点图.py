from randomwalk import Randomwalk
from matplotlib import pyplot as plt

item = Randomwalk()
plt.scatter(item.run(50000), item.run(50000), s=1)
plt.show()



