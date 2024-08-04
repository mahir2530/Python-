# Create a pyramid of user’s choice ,
# User will enter the starting value for printing the pyramid
# User will enter the Ending Value of the pyramid
# Example
# Enter the start value for pyramid : 2
# Enter the end value for pyramid : 4
# * *
# * * *
# * * * *

num1 = int(input("Enter The Starting Value : "))
num2 = int(input("Enter The Ending Value : "))

for i in range(num1,num2 + 1):
        
    print(" " * (num2 - i), end="")
    print(" ".join(["*"] * i))