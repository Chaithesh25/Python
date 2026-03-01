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


import numpy as np
import matplotlib.pyplot as plt

# Create data
x = np.linspace(-3, 3, 50)
y = np.linspace(-3, 3, 50)
X, Y = np.meshgrid(x, y)

Z = np.sin(X**2 + Y**2)

# Create contour plot
plt.contourf(X, Y, Z)

# Add color bar
plt.colorbar(label="Z value")

# Labels and title
plt.title("Simple Contour Plot")
plt.xlabel("X axis")
plt.ylabel("Y axis")

plt.savefig()