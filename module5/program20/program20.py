import numpy as np
import matplotlib.pyplot as plt

def create_3d():
    np.random.seed(0)
    x = np.random.rand(50)
    y = np.random.rand(50)
    z = np.random.rand(50)
    color = np.random.rand(50)


    fig = plt.figure(figsize=(8,6))
    ax = fig.add_subplot(111, projection='3d')


    scatter = ax.scatter(x,y,z, c= color , cmap='viridis', s=60)

    ax.set_xlabel("x variable")
    ax.set_ylabel("y variable")
    ax.set_zlabel("z variable")

    cbar = plt.colorbar(scatter)
    cbar.set_label("four variable")


    plt.savefig("3d scatter plot")

create_3d()