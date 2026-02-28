def remove_occ(list , ele):
    while ele in list:
        list.remove(ele)

    
    return list





list_items = [10,45,32,56,78,34,86,56]
result = remove_occ(list_items,56)
print("new list: ",result)