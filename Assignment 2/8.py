'''Write a program which will show the following operations as 
• All 
• Any 
• Enumerate'''

input = input("Enter elements (separated by space): ")

elements = input.split()
list = []
for element in elements:
    list.append(int(element))

print("All elements are true:", all(list))

print("Any element is true:", any(list))

for i, value in enumerate(list):
    print(f"Index {i}: {value}")
