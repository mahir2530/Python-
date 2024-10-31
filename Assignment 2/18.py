"""Write a Python program that will check whether number inputted is prime 
number or not. """

num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Number is not prime.")
            break
    else:
        print("Number is prime.")
else:
    print("Number is not prime.")
