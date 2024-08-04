'''#1

for i in range(1,5):
    for j in range(1,5):
        print("*",end = "")
   
    print()
'''




'''#2

for i in range(1,5):
    for j in range(1,5):
        print(i,end=" ")
    
    print()
'''




'''#3

for i in range(1,5):
    for j in range(1,5):
        print(j,end=" ")
    
    print()
'''




'''#4

for i in range(1,5):
    for j in range(1,5):
        print(i * j ,end=" ")
    
    print()
'''


    

'''#5

for i in range(4,0,-1):
    for j in range(1,5):
        print(j * i ,end=" ")
    
    print()
'''




'''#6

for i in range(1,5):
    for j in range(i):
        print("*",end = " ")

    print()
'''




'''#7

for i in range(1,5):
    for j in range(i):
        print(i,end = " ")

    print()
'''




'''#8

for i in range(1,5):
    for j in range(i + 1):
        print(j,end = " ")

    print()
'''



'''#9

for i in range(1,5):
    for j in range(1,i + 1):
        print(j * i,end = " ")

    print()
'''



'''#10

num = 1

for i in range(1,5):
    for j in range(i):
        print(num ,end=" ")
        num += 1

    print()
'''




'''#11

for i in range(1,5):
    for j in range(i,0,-1):
        print(j,end = " ")

    print()
'''




'''#12

for i in range(4,0,-1):
    for j in range(4,i-1,-1):
        print(j,end = " ")
    
    print()
'''




'''#13

for i in range(4,0,-1):
    for j in range(i,4 + 1):
        print(j,end = " ")
    
    print()
'''




#14

for i in range(4,0,-1):
    for j in range(i):
        print("*",end = " ")
    
    print()





'''#15

for i in range(1,5):
    for j in range(4-i+1):
        print(i,end = " ")
    
    print()
'''




'''#16

for i in range(4,0,-1):
    for j in range(1,i+1):
        print(j,end = " ")
    
    print()
'''



'''#17

for i in range(1,5):
    for j in range(1,i + 1):
        print(j * i,end = " ")
    
    print()
'''




'''#18

for i in range(4,0,-1):
    for j in range(i):
        print(i,end = " ")

    print()
'''




'''#19

for i in range(4,0,-1):
    for j in range(i,0,-1):
        print(j,end = " ")

    print()
'''




'''#20

for i in range(1,5):
    for j in range(i,4 + 1):
        print(j,end = " ")
    
    print()
'''




'''#21

for i in range(1,5):
    for j in range(5 - i):
        print(" ",end = " ")

    for k in range(i):
        print("*",end = " ")

    print()
'''




'''#22

for i in range(1,5):
    for j in range(5 - i):
        print(" ",end = " ")

    for k in range(i):
        print(i,end = " ")

    print()
'''




'''#23

for i in range(4,0,-1):
    for j in range(4,i - 1,-1):
        print(" ",end = " ")

    for k in range(j):
        print(j,end = " ")

    print()
'''




'''#24

for i in range(4,0,-1):
    for j in range(4 - i):
        print(" ",end = " ")

    for j in range(i,0,-1):
        print(i,end = " ")

    print()
'''




'''#25

for i in range(1,5):
    for j in range(5 - i):
        print(" ",end = " ")

    for k in range(i,0,-1):
        print(k,end = " ")

    print()
'''




'''#26

for i in range(1,5):
    for j in range(5 - i):
        print(" ",end = " ")
 
    for k in range(1,i+1):
        print(k,end = " ")
    print()
'''




'''#27

for i in range(4,0,-1):
    for j in range(5 - i):
        print(" ",end = " ")

    for k in range(i):
        print("*",end = " ")

    print()
'''




'''# 28

for i in range(1,5):
    for j in range(i):
        print(" ",end = " ")

    for k in range(i,5):
        print(k,end = " ")

    print()
'''




'''#29

for i in range(4,0,-1):
    for j in range(5 - i):
        print(" ",end = " ")

    for k in range(i):
        print(i,end = " ")

    print()
'''




'''#30

for i in range(1,5):
    for j in range(i):
        print(" ",end = " ")

    for k in range(i):
        print(k,end = " ")

    print()
'''




'''#31

for i in range(4,0,-1):
    for j in range(4 - i):
        print(" ",end = " ")

    for k in range(i,0,-1):
        print(k,end = " ")

    print()
'''




'''#32

num = 1

for i in range(1,5):
    for j in range(i):
        print(" ",end = " ")

    for k in range(1,5):
        print(num,end = " ")
        num += 1

    print()
'''



'''#33

for i in range(1,6):
    for j in range(i):
        if(i + j)%2==0:
            print(1,end = " ")
        else:
            print(0,end=" ")
    
    print()
'''

'''r = 5

for i in range(r):
    for j in range(r - i - 1):
        print(" ",end = '')
    
    for k in range(i + 1):
        if i%2 == 0:
            print("0 ",end="")
        else:
            print("1 ",end="")

    print()
'''


# for i in range(5,0,-1):
#     for j in range(i,0,-1):
#         print(j,end=" ")
    
#     print()