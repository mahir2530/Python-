'''Make a list by taking 10 input from user. Now delete all the repeated elements of the 
list: 
Input: [1,2,3,2,1,3,12,12,32,1] 
Output: [1,2,3,12,32] '''

input = []
for i in range(10):
    element = int(input(f"Enter element {i+1}: "))
    input.append(element)

print("before Remove:", input)

# Remove duplicates
remove = []
for element in input:
    if element not in remove:
        remove.append(element)

print("After Remove:", remove)