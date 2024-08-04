'''num = int(input('Enter The Number : '))

if (num % 2) == 0:
    print('{0} is Even '.format(num))

else:
    print('{0} is Odd '.format(num))'''


# Using For Loop.........

'''sum = 0
sum1 = 0

for i in range(1,10):
    if i%2 == 0:
        print(i)
        sum += i

    else:
        print(i)
        sum1 += i
    
    
    
print("Sum of Even Number : ",sum)
print("Sum of Odd Number : ",sum1)'''


osum = 0
esum = 0
ocount = 0
ecount = 0


for i in range(1, 11):
    
    if i % 2 != 0:
    
        print(i, end="\t\t\t")

        osum += i
        ocount += 1
        
        if i < 10:
            
            print(i + 1)
            
            esum += i + 1
            ecount += 1


print("osum=" , osum , "\t\t" , "esum=" , esum)
print("ocount=" , ocount , "\t\t" , "ecount=" , ecount)
