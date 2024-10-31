'''Write a Pytthon program that will ask the user to input a three digit number 
and make sum of that and display the sum.'''

num=int(input("Enter a three digits number : "))

sum=0
while num !=0:
    digit=num%10
    sum+=digit
    num//=10
print("The sum of three digits is : ",sum)