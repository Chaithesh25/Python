def remove_vowels(str):
    vowels = "aeiouAEIOU"
    store = ""
    for ch in str:
        if ch  not in vowels:
            store += ch

    return store 

    




string = input("enter a string: ")
print("Result is : ",remove_vowels(string))