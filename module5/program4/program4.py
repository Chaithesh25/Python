import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1,6)
y = [10,20,30,40,50]
error = [1,0.5,2,1.5,1]

plt.errorbar(x,y,yerr=error , fmt='-o' , capsize= 5)

plt.title("error line plot")
plt.xlabel("xvalue")
plt.ylabel("y values")

plt.grid(True)
plt.savefig("errorplot")