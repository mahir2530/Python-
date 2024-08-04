num1 = int(input("Enter The First Number : "))
num2 = int(input("Enter The Second Number : "))
num3 = int(input("Enter The Third Number : "))

if num1 > num2 and num1 > num3:
    print("First Number is Greater than Second and Third")

elif num2 > num1 and num2 > num3:
    print("Second Number is Greater than First and Third")

elif num3 > num1 and num3 > num2:
    print("Third Number is Greater than Second and First")
