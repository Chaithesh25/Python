import matplotlib.pyplot as plt


def create_plots(height,weight):

    plt.scatter(height,weight, color ='blue', marker='o',label ="height vs weight")

    plt.xlabel("height")
    plt.ylabel("weight")
    plt.title("scatter plot")

    plt.legend()

    plt.grid(True)
    plt.savefig("scatterplot")

  





height = [160,165,170,175,180,185]
weight = [ 20,30,49,50,60,70]


create_plots(height,weight)