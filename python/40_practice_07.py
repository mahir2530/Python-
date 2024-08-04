#Assignment Operation

a = 20
b = 15

c = a
print("Assign : ", c)

c += b 
print("Add and Assign : ", c)

c -= b
print("Subtract and Assign : ", c)

c *= b
print("Multiply and Assign : ", c)

c /=  b
print("Div and Assign : ", c)

c %= b
print("Modulus and Assign:", c)

c **= b
print("Exponentiation and Assign:", c)

c //= b
print("Floor Division and Assign:", c)


#Logical Operation

print("Logical AND:", a > 0 and b > 0)
print("Logical OR:", a > 0 or b < 0)
print("Logical NOT:", not(a > 0))