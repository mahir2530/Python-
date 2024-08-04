r = int(input("Enter The Number of Rows : "))
c = int(input("Enter The Number of Colums : "))

matrix = []

print("Enter The Enteries Row-wise : ")
for i in range(r):
    a = []
    for j in range(c):
        a.append(int(input("Enter The Value : ")))
    matrix.append(a)

print("Array : ")
for i in range(r):
    for j in range(c):
        print(matrix[i][j], end = " ")
    print()

odd_numbers = []
even_numbers = []

for r in matrix:
    for num in r:
        if num%2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)

print("Even Numbers : ", even_numbers)
print("Odd Numbers : ", odd_numbers)

