import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
data = np.random.normal(loc=50 ,scale=10,size=200)

def create_bins(data,bins):
    plt.figure(figsize=(7,5))
    plt.hist(data,bins=bins)
    plt.title("histogram")
    plt.xlabel("values")
    plt.ylabel("freqencyy")

    plt.savefig("histogram")


# create_bins(data,bins=5)
# create_bins(data,bins=15)
create_bins(data,bins=30)