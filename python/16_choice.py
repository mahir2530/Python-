a = int(input('Enter The Value of A : '))
b = int(input('Enter The Value of B : '))

print("1. Sum : ")
print("2. Sub : ")
print("3. Multi : ")
print("4. Div : ")
print("5. Exit :")

ch = int(input("Enter Your Choice : "))

if ch == 1:
    print('Sum : ',a + b)
elif ch == 2:
    print('Sub : ',a - b)
elif ch == 3:
    print('Multi : ',a * b)
elif ch == 4:
    print('Div : ',a / b)
elif ch == 5:
    print('Exit : ')
