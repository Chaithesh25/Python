import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt


def create_boxplot():

    data = {
        "categroy":['A','A','A','A','B','B','B','B','C','C','C','C'],
        "values" : [16,14,35,]
    }

    df = pd.DataFrame(data)
    sn.set_style("whitegrid")

    plt.fugure(figsize=(8,5))
    sn.boxplot(x="categories", y ="values", data = df , palette = ['lightgreen','yellow','salmon'],filerprops = dict(marker = 'o', markerfacecolor = 'red', markersize = 12) )
    

    plt.title("boxplot")
    plt.xlabel("catgeories")
    plt.ylabel("values")

    plt.savefig("boxplot")

create_boxplot()



