def count_frequency(number):
    freq = {}
    for num in number:
        if num in freq:
            print("already exists")
            freq[num] +=1 
            print(freq[num])
            # freq[num]
        else:
            print("not exists")
            freq[num] = 1
            print(num)
    
    return freq
           
    
           





list_items = list(map(int ,input("enter list items: ").split()))

result = count_frequency(list_items)

print(result)


