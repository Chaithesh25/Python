import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10,100)

y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)


plt.figure(figsize=(8,6))

plt.plot(x, y1 , label = "sin(x)", linewidth = 2)
plt.plot(x, y2 , label = "cos(x)", linewidth = 2)
plt.plot(x, y3 , label = "tan(x)", linewidth = 2)

plt.title("multi line plot")
plt.xlabel("x values")
plt.ylabel("y values")
plt.legend(title = "functions" , loc = "upper right")
plt.grid(True)


plt.savefig("multipleplot")