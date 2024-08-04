list1 = ["RED", "BLUE", "GREEN"]

list1.append("BLACK")
print("\nAfterv Adding Black : ",list1)

list1.extend([2, 3, 4])
print("\nAfter Adding [2, 3, 4] : ", list1)

list1 = [str(item) for item in list1]
list1.sort()

print("\nAfter Sorting : ", list1)
print("\n")