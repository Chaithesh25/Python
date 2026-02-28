num = list(map(int, input("enter the number seperated by space: ").split()))
print(num)



for i in num:

    if( i < 0):
        continue

    if (i % 2 == 0):
        print(i)
        continue