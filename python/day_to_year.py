days = int(input("Enter The Days : "))

y = days / 365
m = (days % 365) / 30
rd = (days % 365) % 30

print("Year : ",y)
print("Month : ",m)
print("Reminder Days : ",rd)
