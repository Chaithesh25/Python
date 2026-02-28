def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)


num = int(input("Enter the number: "))

if(num < 0):
    print("number cannot be negetive or zero")
else:
    print("fibonaccchi series are: ")
    for i in range(num):
        print(fibo(i))
    
