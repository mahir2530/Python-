class BankAccount:

	acc_no=154266
	balance=10000
	date_of_oepening=15-12-2004
	cust_name='Shubham'

	def deposit(self,amount):

		self.balance=self.balance+amount


	def withdrawl(self,amount):

		if amount>self.balance:

			print("")
			print("Insufficient Balance")
			print("")

		else:
			self.balance=self.balance-amount


	def checkbalance(self):

		print("")
		print("Total Balance : ",self.balance)
		print("")


b1=BankAccount()

while True:

	ch=int(input('Enter Choice : '))

	if ch==1:

		print()
		dep=int(input('Enter Deposit Amount : '))
		print()

		b1.deposit(dep)

	elif ch==2:

		print()
		wit=int(input('Enter Withdrawl Amount : '))
		print()

		b1.withdrawl(wit)


	elif ch==3:

		print()
		b1.checkbalance()
		print()


	elif ch==4:

		print()
		print('Exiting')
		print()
		break
