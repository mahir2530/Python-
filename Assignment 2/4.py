# Write a Python program that will find greatest of three numbers using elif conditional 
# statement. 

n1=int(input("Enter number 1 : "))
n2=int(input("Enter number 2 : "))
n3=int(input("Enter number 3 : "))

if n1 > n2 and n1>n3 :
    print("n1 is greter")
elif n2 > n1 and n2>n3 :
    print("n2 is greter")
else:
    print("n3 is greter")
