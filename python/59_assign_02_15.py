list1 = []

for i in range(10):
    element = input(f"Enter {i} Index Number : ")
    list1.append(element)

remove_duplicate = list(set(list1))

remove_duplicate.sort()

print("List After Removing Duplicates Item : ", remove_duplicate)
