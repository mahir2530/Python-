a = int(input("Enter a number to check if it's perfect: "))

sum = 0

for i in range(1,a):
    if a%i == 0:
        sum = sum + i
        print(i)

print("Sum : ",sum," Original : ",a)
if sum == a:
    print("This is Perfect Number...")
else:
    print("This is Not Perfect Number...")
