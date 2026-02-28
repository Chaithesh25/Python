list1  = list(map(int, input("Enter the elements list1 : ").split()))
list2  = list(map(int, input("Enter the elements list2 : ").split()))


set1 = set(list1)
set2 = set(list2)

union = set1.union(set2)
intersection = set1.intersection(set2)

print(f"set 1 : {set1}")
print(f"set 2 : {set2}")

print("union: ",union)
print("intersection: ",intersection)
