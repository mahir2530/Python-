rows = int(input("Enter The Number of Rows : "))
cols = int(input("Enter The Number of Colums : "))

matrix = []
print("Enter The Element Row by Col : ")

for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input(f"Element [{i}][{j}] : "))
        row.append(element)
    matrix.append(row)

max_value = []
min_value = []

for i in range(rows):
    for j in range(cols):
        if matrix[i][j] > element:
            max_value = element
        else:
            min_value = element

print("Matrix:")
for row in matrix:
    print(row)

print("Maximum elements:", max_value)
print("Minimum elements:", min_value)