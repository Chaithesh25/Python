import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0,10,100)
y1 = np.sin(x)
y2 = np.cos(x)


plt.rcParams['font.family'] = 'DejaVu sans'
plt.rcParams['font.size'] = 12

brand_color = {
    'primary' : "blue",
    'secondary':"green",
    'background':"yellow",
    'grid' : "red"
}

plt.figure(figsize=(8,10))
plt.gca().set_facecolor(brand_color["background"])

plt.plot(x,y1,label = 'sinwave',color = brand_color["primary"],linewidth = 3)
plt.plot(x,y2,label = 'cosin wave', color = brand_color["secondary"],linewidth= 2)
plt.grid(True , color = brand_color["grid"], linestyle ='--',linewidth = 0.8)

plt.title("customixed", fontsize = 12 , fontweight  = 'bold')


plt.legend()
plt.tight_layout()
plt.savefig("customized")