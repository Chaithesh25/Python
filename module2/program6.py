name = input("enter your name: ")
age = int(input("Enter your age: "))
city = input("enter your city: ")

# using format
output1 = "my name is {}, my age is {} my city is {}".format(name,age,city)

# using fstring
output2 =f"my name is {name}, my age is {age}, my city is  {city}"


print("using format: ",output1)
print("using fstring: ",output2)