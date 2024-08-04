n = int(input("Enter The Number : "))

t = 0

for i in range(2,n):
    if n%i==0:
        t = 1

if t == 1:
    print("Number is Not Prime...")
else:
    print("Number is Prime...")

