def recurs(n):

	if n==0:
		return 0

	else:
		return n+recurs(n-1)


print("Addition of 0 To 10 : ",recurs(10))