import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0,10,100)
y = np.sin(x)
data = np.random.randn(100)

fig, ax = plt.subplots(2,2, figsize=(8,6))

ax[0, 0].plot(x,y)
ax[0, 0].set_title("line plott")

ax[0, 1].scatter(x,y)
ax[0, 1].set_title("scatter plot")


ax[1, 0].hist(data)
ax[1, 0].set_title("histogram")


ax[1, 1].bar(['A','B','C'],[10,20,30])
ax[1, 1].set_title("barchart")


plt.tight_layout()
plt.savefig("multipleplot")