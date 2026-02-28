x = 10

def modify():
    global x
    x = 20
    print("inside function variable x: ",x)


modify()

print("variable outside function :",x)