
while True:

	try:

		num=int(input("Enter Your Age : "))

		print("Your Age Is : ",num)
		break;

	except ValueError:

		print(" ")
		print("ERROR PLZ ENTER NUMERIC VALUE")
		print(" ")