# Create a Dictionary to store the student’s detail like name, roll_no, contact, email.
# • Check weather roll_no is there or not in dictionary.
# • Print the Dictionary.

students = {
    'name': 'John Doe',
    'roll_no': '123',
    'contact': '555-1234',
    'email': 'john.doe@example.com'
}

roll_no_to_check = '123'

if 'roll_no' in students and students['roll_no'] == roll_no_to_check:
    print(f"Roll number {roll_no_to_check} is in the dictionary.")
else:
    print(f"Roll number {roll_no_to_check} is not in the dictionary.")

print(students)
