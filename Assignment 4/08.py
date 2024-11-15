class Student:

	def __init__(self,name,rollno,sem):

		self.name=name
		self.rollno=rollno
		self.sem=sem


	def display(self):

		print("")
		print("Student Name : ",self.name)
		print("Student Rollno : ",self.rollno)
		print("Student Class : ",self.sem)



stu1=Student('Shubham',70,5)
stu1.display()


stu2=Student('Nandish',113,5)
stu2.display()