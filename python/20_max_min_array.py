a = []
n = int(input("Emter The Range of Array : "))

for i in range(n):
    b = int(input("Enter The Number : "))
    a.append(b)

maxvalue = a[0]
minvalue = a[0]

for i in range(n):
    if (a[i] > maxvalue):
        maxvalue = a[i]
    if (a[i] < minvalue):
        minvalue = a[i]

print("Maxvalue : ",maxvalue)
print("Minvalue : ",minvalue)