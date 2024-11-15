try:

	num=int(input("Enter A Number: "))

	if num<0:
		raise ValueError("Error , Plz Enter Possitive Number")

	print("Possitive Number ",num)

except ValueError as e:

	print(e)