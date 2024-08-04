# Create a list to store Employee Id, Name, Salary and Designation and perform the
# following operation.
# - If salary is grater than 30,000 than increase the HRA for 5%, and Medicliam for 10%.
# - If salary is grater than 50,000 than increase the HRA for 7%, and Medicliam for 12%.
# - If salary is grater than 80,000 than increase the HRA for 10%, and Medicliam for
# 15%.
# - Print only name and designation with the help of slicing operation.

employees = [
    {"Employee Id": 1, "Name": "mno", "Salary": 35000, "Designation": "Software Engineer", "HRA": 0, "Mediclaim": 0},
    {"Employee Id": 2, "Name": "xyz", "Salary": 55000, "Designation": "Project Manager", "HRA": 0, "Mediclaim": 0},
    {"Employee Id": 3, "Name": "abc", "Salary": 85000, "Designation": "Director", "HRA": 0, "Mediclaim": 0},
    {"Employee Id": 4, "Name": "pqr", "Salary": 25000, "Designation": "Intern", "HRA": 0, "Mediclaim": 0}
]

for employee in employees:
    salary = employee["Salary"]
    
    if salary > 80000:
        employee["HRA"] += salary * 0.10
        employee["Mediclaim"] += salary * 0.15
    elif salary > 50000:
        employee["HRA"] += salary * 0.07
        employee["Mediclaim"] += salary * 0.12
    elif salary > 30000:
        employee["HRA"] += salary * 0.05
        employee["Mediclaim"] += salary * 0.10

for employee in employees:
    print(employee["Name"], employee["Designation"])

# for employee in employees:
#     print(employee)
