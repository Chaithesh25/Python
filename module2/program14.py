age = {
    "chaithesh" : 22,
    "anish" : 24,
    "harshith": 35,
    "manoj": 40,
    "astern": 45
}

def get_name(name):

    return age[name]



name = input("enter the name : ")
print("age : ",get_name(name))