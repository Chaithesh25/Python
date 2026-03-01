import pandas as pd
import seaborn as sn
import numpy as np
import matplotlib.pyplot as plt


np.random.seed(0)

data = {
    'maths': np.random.randint(50,100,20),
    'science':np.random.randint(45,95,20),
    'English':np.random.randint(40,90,20),
    'History':np.random.randint(55,100,20)
}

df = pd.DataFrame(data)

corr = df.corr()


plt.figure(figsize=(8,6))
sn.heatmap(corr,annot=True,cmap="coolwarm",fmt='.2f',linewidths=0.5)

plt.title("heatmap")
plt.xticks(rotation = 45)
plt.yticks(rotation = 0)

plt.savefig("heapmap")