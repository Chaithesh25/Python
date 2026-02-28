def converter(tup):
    even_list = []

    for num in tup:
        if num % 2 == 0:
            even_list.append(num)
    
    new_tupple = tuple(even_list)
    return new_tupple




numbers = tuple(map(int ,input("Enter a numbers: ").split()))
result = converter(numbers)
print("Even number tuple elements are : ",result)




