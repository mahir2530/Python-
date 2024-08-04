arr = []

n = int(input("Enter The Range of Array : "))

for i in range(n):
    b = int(input(f"Enter The [{i}] Element : "))
    arr.append(b)

print("Array : ")
print(arr)

if len(arr) < 2:
    print("Array Does not Have Enough Element : ")
else:
    largest = second_largest = float('-inf')

    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        
        elif num > second_largest and num != largest:
            second_largest = num

    if second_largest == float("-inf"):
        print("There is no Second Laargest...")
    else:
        print("The Second Largest Element is : ", second_largest)