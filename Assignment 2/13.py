'''Write a program which will display the use of the following function 
• Replicating Tuple 
• Slicing Tuple 
• Search an item with its index '''


item = int(input("Enter the number of items for the tuple: "))

tuple = ()

for i in range(item):
    value = int(input(f"Enter value {i+1} for the tuple: "))
    tuple += (value,)

factor = int(input("Enter the replication factor: "))
replicated = tuple * factor
print("Replicated tuple:", replicated)

start = int(input("Enter the start index for slicing: "))
end = int(input("Enter the end index for slicing: "))
sliced = tuple[start-1:end]
print("Sliced tuple:", sliced)

serach = int(input("Enter the value to search: "))

if serach in tuple:
    index = tuple.index(serach)
    print(f"Index of {serach}: {index}")
else:
    print(f"{serach} not found in the tuple.")