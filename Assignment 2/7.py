"""Write a program which will perform following function on tuple 
• Max and min value from list 
• Length of the list 
• Sorting a list 
• Sum of list item """

num = input("Enter elements (separated by space): ")

elements = num.split()

val = tuple(int(element) for element in elements)

print(type(val))

print("===============|MIN & MAX|=====================")
print("Max element is:", max(val))
print("Min element is:", min(val))

print("===============|SORT|=====================")
print(sorted(val))

print("===============|SUM|=====================")
print(sum(val))

