def outer(a,b):

	def inner():
		add=a+b
		return add


	return inner()+5



print("RESULT = ",outer(5,5))