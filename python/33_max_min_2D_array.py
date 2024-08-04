r = int(input("Enter The Number of Rows : "))
c = int(input("Enter The Number of Colums : "))

matrix = []

print("Enter The Value Row-wise :: ")
for i in range(r):
    a = []
    for j in range(c):
        a.append(int(input("Enter The Number : ")))
    matrix.append(a)

print("2D Array : ")
for i in range(r):
    for j in range(c):
        print(matrix[i][j], end = " ")
    print()

max_number = a[0]
min_number = a[0]

for r in matrix:
    for num in r:
        if num > max_number:
            max_number = num
        if num < min_number:
            min_number = num

print("Maximum Number : ", max_number)
print("Minimum Number : ", min_number)