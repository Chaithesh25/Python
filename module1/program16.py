num = int(input("Enter a number to reverse: "))
reversed_number = 0
i = 0
print(len(str(num)))


while num > 0:
         digit = num % 10
         reversed_number = reversed_number * 10 + digit
         num = num // 10
        


print(f"reversed number is :{reversed_number} ")
