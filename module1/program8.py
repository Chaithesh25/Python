user_input = input("Enter the elements seperated by spaces: \n")
elements = user_input.split()
data = 0


for i in elements:
    if i.isdigit():
        data += int(i)



print("converted list is : ",data)

