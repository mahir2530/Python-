"""Write a Pytthon program that will calculate the Basic Salary of an employee 
where : 
1. HRA is 10% of Basic Salary 
2. DA is 20% of Basic Salary 
3. TA is 10% of Basic Salary 
4. PF is 20 % of Basic Salary 
5. Also calculate the net salary of the employee. """

salary=float(input("Enter Your Basic Salary : "))

HR=salary*0.10
DA=salary*0.20
TA=salary*0.10
PF=salary*0.20

net_Salary= salary+HR+DA+TA-PF

print("YOUR NET SALARY IS : ",net_Salary)


