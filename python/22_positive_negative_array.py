a = []
poscount = 0
negcount = 0
zerocount = 0

n = int(input("Enter The Range of Array : "))

for i in range(n):
    b = int(input("Enter The Value : "))
    a.append(b)

for i in range(n):
    if a[i] > 0:
        print("The Number is Positive : " , a[i])
        poscount += 1
    elif a[i] == 0:
        print("The Number is Zero : " , a[i])
        zerocount += 1
    else:
        print("The Number is Negative : " , a[i])
        negcount += 1

print("Positive Number Count : " ,poscount)
print("Zero Number Count : " ,zerocount)
print("Negative Number Count : " ,negcount)

