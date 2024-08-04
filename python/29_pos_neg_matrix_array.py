rows = int(input("Enter The Number of Rows : "))
cols = int(input("Enter The Number of Colums : "))

matrix = []
print("Enter The Element Row by Col : ")

for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input(f"Element [{i}][{j}]"))
        row.append(element)
    matrix.append(row)

pos_element = []
neg_element = []

for i in range(rows):
    for j in range(cols):
        if matrix[i][j] >= 0:
            pos_element.append(matrix[i][j])
        else:
            neg_element.append(matrix[i][j])

print("Matrix:")
for row in matrix:
    print(row)

print("Positive elements:", pos_element)
print("Negative elements:", neg_element)

