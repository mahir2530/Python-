try:

	num1=int(input("Enter Num1 : "))
	num2=int(input("Enter Num2 : "))

	print("Division : ",num1/num2)

except ZeroDivisionError:

	print("ERROR PLZ ENTER NON-ZERO VALUE IN NUM2")