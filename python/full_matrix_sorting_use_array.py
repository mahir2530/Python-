rows = int(input("Enter The Number of Row : "))
cols = int(input("Enter The Number of Colum : "))

matrix = []
print("Enter The Element Row by Colum : ")

for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input(f"Element [{i}][{j}]"))
        row.append(element)
    matrix.append(row)

print("Matrix : ")
for row in matrix:
    print(row)

asc = matrix.sort()
desc = matrix.sort(reverse=True)

print(asc)
print(desc)