try:

	num1=int(input("Enter Num1 : "))
	num2=int(input("Enter Num2 : "))

	if num2==0:
		raise Exception("ERROR PLZ ENTER NON-ZERO VALUE IN NUM2")

	print("Division : ",num1/num2)

except Exception as e:

	print("")
	print(e)
	print("")