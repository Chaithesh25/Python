string = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for ch in string:
    if ch in vowels:
        count = count+1


print(f"total count of vowels in the string is : {count}")