def factor(num): 
    print(f"Factor of {num} : ")
    for i in range(1,num + 1):
        if num % i == 0:
            print(i, end = " ")
    print()

num = int(input("Enter The Number : "))

fac = factor(num)
print(fac)