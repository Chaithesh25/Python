import matplotlib.pyplot as plt
import numpy as np

data = [
    [10,22,34,56],
    [58,60,62,64],
    [67,69,71,75],
    [76,78,80,82],
    [84,86,88,90]
]

data = np.array(data)

mean = np.mean(data,axis=1)
std = np.std(data,axis=1)

x = np.arange(1 , len(mean) + 1)


plt.errorbar(x , mean , yerr= std,fmt='o-' ,capsize= 5)

plt.title("prgam5")
plt.xlabel("x values")
plt.ylabel("y values")

plt.grid(True)
plt.savefig("meanstandard deviation")