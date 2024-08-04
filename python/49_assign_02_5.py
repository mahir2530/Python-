def sumthreenum(number):
    sum = 0

    if 100 <= number <= 999:
        while number > 0:
            sum += number % 10
            number //= 10

        return sum
    
    else:
        return None

num = int(input("Enter The Number : "))

result = sumthreenum(num)

print(result)