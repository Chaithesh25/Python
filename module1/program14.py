numbers = list(map(int, input("enter the numbers: ").split()))

maximum = max(numbers)
minimum = min(numbers)
sum = sum(numbers)
sorted_list = sorted(numbers)


print("maximum number in the list: ",maximum)
print("minimum number in the list: ",minimum)
print("sum of all the numbers: ",sum)
print("orignial list : ",numbers)
print("sorted list: ",sorted_list)
