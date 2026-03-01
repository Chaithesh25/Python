import pandas as pd




def addbonus(data):

    data['bonus'] = data["salary"] * 0.10

    return data


data = {
    'name': ["chaithesh","astern","avin"],
    'departmanet' : ['it','hr','it'],
    'salary' : [100000,200000,300000]
}

df = pd.DataFrame(data)

print("original data: ",df)
df = addbonus(df)
print(df)
