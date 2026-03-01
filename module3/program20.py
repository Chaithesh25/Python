import numpy as np
import pandas as pd

data1 = {
    "emp_id":[101,102,103,104],
    "name":['chaithesh','astern','avin','manoj'],
    "Department":['it','hr','clerk','it']
}

data2 = {
     "emp_id":[101,102,103,104],
     "salary":[10000,20000,40000,30000]   
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)


print(df1)
print(df2)


innerjoin = pd.merge(df1,df2,on='emp_id' ,how='inner')
leftjoin = pd.merge(df1,df2, on='emp_id', how='left')
rightjoin = pd.merge(df1,df2, on='emp_id', how='right')


print(innerjoin)
print(leftjoin)
print(rightjoin)