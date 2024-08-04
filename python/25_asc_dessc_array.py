arr = []

n = int(input("Enter The Range of Array : "))

for i in range(n):
    b = int(input("Enter The Number : "))
    arr.append(b)

arr.sort()
print("Array in Ascending : ", arr)

arr.sort(reverse=True)
print("Array in Descending : ", arr)
