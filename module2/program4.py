def reversed_firs_half_join(str):
    mid = len(str) //2

    first_half = str[:mid]
    second_half = str[mid:]
    print("first half: ",first_half)
    print("second_half",second_half)

    reversed_firs_half_variable = first_half[::-1]
    print(reversed_firs_half_variable)

    joined = reversed_firs_half_variable + second_half

    return joined
 




string = input("Enter a string : ")
result = reversed_firs_half_join(string)
print(f"Result :{result} ")
