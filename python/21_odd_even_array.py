arr = []
n = int(input("Enter The Range of Array : "))

for i in range(n):
    b = int(input("Enter The Number : "))
    arr.append(b)

odd_count = 0
even_count = 0
odd_sum = 0
even_sum = 0

for i in range(n):
    if arr[i] % 2 == 0:
        even_count += 1
        even_sum += arr[i]
    else:
        odd_count += 1
        odd_sum += arr[i]

print("Count of Odd Number : ",odd_count)
print("Sum of Odd Number : ",odd_sum)
print("\nCount of Even Number : ",even_count)
print("Sum of Even Number : ",even_sum)