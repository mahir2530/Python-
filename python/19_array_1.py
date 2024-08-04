a = []
sum = 0
n = int(input("Enter The Value : "))

for i in range(n):
    b=int(input("enter value="))
    a.append(b)

for i in range(n):
    print(a[i])
    sum = sum + a[i]

print("sum=",sum)