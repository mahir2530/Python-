try:

	num=int(input("Enter Your Age : "))

	print("Your Age Is : ",num)

	if num<0:
		raise Exception("ERROR PLZ ENTER POSSITIVE VALUE")

except Exception as e:

	print("")
	print(e)
	print("")