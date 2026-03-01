import pandas as pd

data = {
    'name': ['chaithesh','avin','asterb'],
    'age':[20,34,22],
    'number':[1,2,3]
}

df = pd.DataFrame(data)

print(df)

print("first row: ",df.head())