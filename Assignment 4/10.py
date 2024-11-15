class Employee:

	def __init__(self,emp_id, emp_name, emp_salary,emp_department):

		self.emp_id=emp_id
		self.emp_name=emp_name
		self.emp_salary=emp_salary
		self.emp_department=emp_department


	def calculate_emp_salary(self,hours):

		if self.emp_salary > hours :

			new_salary = self.emp_salary + (self.emp_salary*0.1)

			self.emp_salary=new_salary


	def emp_assign_department(self):

		new_dep="Managing"

		self.emp_department=new_dep


	def print_employee_details(self):

		print("")
    
		print("Id : ",self.emp_id)

		print("Name : ",self.emp_name)

		print("Department : ",self.emp_department)

		print("Salary : ",self.emp_salary)

		print("")


e1=Employee(101,'shubham',150000,"Packing")


e1.calculate_emp_salary(52)

ch=input("Do You Want To Change The Department (y/n) : ")

if ch=='y':

	e1.emp_assign_department()


e1.print_employee_details()


