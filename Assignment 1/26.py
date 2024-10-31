'''Write a Python program which will have Main Menu for performing following operations
based on selection:
Main Menu:
Airthmetic Operation
Identity Operator Operation
Logical Operation
Member Operator Operation'''

print("Main Menu:")
print("1. Arithmetic Operation")
print("2. Identity Operator Operation")
print("3. Logical Operation")
print("4. Member Operator Operation")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    print("You selected Arithmetic Operation")
    print()
    a=(int(input("Enter a value : ")))
    b=(int(input("Enter b value : ")))
    result=a+b
    print("Result is : ",result)

elif choice == 2:
    print("You selected Identity Operator Operation")
    print()
    a=(int(input("Enter a value : ")))
    b=(int(input("Enter b value : ")))
    print("A is B",a is b)
    print("A is not B",a is not b)

    
elif choice == 3:
    print("You selected Logical Operation")
    print()
    a=(int(input("Enter a value : ")))
    b=(int(input("Enter b value : ")))
    print("A And B",a and b)
    print("A OR B",a or b)
    # print("A NOT B",a ~ b)

elif choice == 4:
    print("You selected Member Operator Operation")
    print()
    a = int(input("Enter a value: "))
    b = input("Enter a value for b: ")

    print("A is in B:", str(a) in b)
    print("A is not in B:", str(a) not in b)

    
else:
    print("Invalid choice")
