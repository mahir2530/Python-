try:

	num1=int(input("Enter Num1 : "))
	num2=int(input("Enter Num2 : "))

	ans=num1/num2

except ZeroDivisionError:

	print("")
	print("ERROR PLZ ENTER NON-ZERO VALUE IN NUM2")

else:

	print(ans)

finally:
	print("This Is Comnpulsory")