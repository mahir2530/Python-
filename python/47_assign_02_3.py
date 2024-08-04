num = int(input("Enter The Number : "))

reversed_num = 0

while num > 0:
    reminder = num % 10
    reversed_num = (reversed_num * 10) + reminder
    num //= 10

print("Reversed Number : ",reversed_num)