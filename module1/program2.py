# num = int(input("enter the numbers"));
# isprime = True

# for i in range(2,num):
#     if(num % i ) == 0:
#         isprime = False
#         break

# if not isprime:
#     print("is not a prime number")
# else:
#     print("given number is prime number")


# using while loop

num = int(input("enter the Element: "))
isprime = True
if(num < 0):
    print("given number is not a prime number!!!!")
else:
    i = 2
    while( i < num):
        if(num % i == 0):
            isprime = False
        i = i + 1
            
if not isprime:
     print("given number is not a prime")

else:
    print("given number is prime number")

   
