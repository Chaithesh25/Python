import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn


data = np.random.normal(loc=50, scale=10 , size=200)

sn.set_style("whitegrid")

plt.figure(figsize=(8,5))

sn.histplot(data, bins=20 , kde=True , color='lightgreen')

plt.title("histogram with kde")
plt.xlabel("values")
plt.ylabel("frequncy")

plt.savefig("histt")