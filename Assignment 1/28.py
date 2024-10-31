'''Write a Python program which asks the user to input a string and perform lstrip and rstrip
function on input string.'''

input_string = input("Enter a string: ")

left = input_string.lstrip()
print("Left stripped string:", left)


right = input_string.rstrip()
print("Right stripped string:", right)

