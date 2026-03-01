import pandas as pd
import numpy as np

data = {
    'name':['chaithu','astern','avin','manoj'],
    'age' : [20,np.nan,34,21],
    'salary':[1200,3400,np.nan,4500],
    'number':[np.nan, 23,45,22]
}

df = pd.DataFrame(data)
print(df.isnull().sum)

df['age'].fillna(df['age'].mean(),inplace=True)
df['salary'].fillna(df['salary'].median(),inplace=True)
df['number'].fillna(df['number'].mode()[0], inplace = True)


df = df.dropna()


print("New dataframe",df)
