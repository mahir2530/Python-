arr1 = []
arr2 = []

n = int(input("Enter The Range Of First Array : "))

for i in range(n):
    x = int(input("Enter The Number of First Array : "))
    arr1.append(x)

m = int(input("\n\nEnter The Range of Second Array : "))

for i in range(m):
    y = int(input("Enter The Number of Second Array : "))
    arr2.append(y)


if len(arr1) != len(arr2):
    print("Error : Length of Both Array are Not Same...")
else:
    result = []

    for i in range(len(arr1)):
       result.append(arr1[i] + arr2[i])

    print("Sum of Two Array : ",result)