'''Write a program which will show the following operations on 
• Dictionary: 
• Return all the keys elements of dictionary 
• Return all the values elements of dictionary 
• Return all the item of a dictionary '''

items = int(input("Enter the number of items: "))

fruit_dict = {}

for i in range(items):
    key = input(f"Enter fruit {i+1}: ")
    value = int(input(f"Enter quantity of {key}: "))
    fruit_dict[key] = value

print("Keys:", fruit_dict.keys())
print("Values:", fruit_dict.values())
print("Items:", fruit_dict.items())