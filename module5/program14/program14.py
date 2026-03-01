import seaborn as sn
import matplotlib.pyplot as plt

def create_pairplot():

    data = sn.load_dataset("iris")

    sn.pairplot(data,
                hue="species",
                diag_kind="hist",
                markers=['o','s','D']
                )
    
    plt.suptitle("pair plot with iris data set",y=1.02)
    plt.savefig("pairplot")


create_pairplot()