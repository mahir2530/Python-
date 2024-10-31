'''Write a program which will show the following operations on Dictionary: 
• Delete an item 
• Compare two dictionaries 
• Remove the all item in dictionary '''


item = int(input("Enter the number of items for dictionary 1: "))

dict1 = {}

for i in range(item):
    key = input(f"Enter key {i+1} for dictionary 1: ")
    value = int(input(f"Enter value for {key}: "))
    dict1[key] = value

item = int(input("Enter the number of items for dictionary 2: "))

dict2 = {}

for i in range(item):
    key = input(f"Enter key {i+1} for dictionary 2: ")
    value = int(input(f"Enter value for {key}: "))
    dict2[key] = value

delete = input("Enter a key to delete from dictionary 1: ")
if delete in dict1:
    del dict1[delete]
    print(f"After deleting '{delete}':", dict1)
else:
    print(f"'{delete}' not found in dictionary 1.")

print("Are dict1 and dict2 equal?", dict1 == dict2)

dict1.clear()
print("After clearing dict1:", dict1)