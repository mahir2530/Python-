'''Write a Python program that will ask the user to input a 3 digit number and 
reverse it '''

# Reverse a 3-digit number
num = int(input("Enter a 3-digit number: "))
reversed_num = 0
while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10
print("Reversed number:", reversed_num)