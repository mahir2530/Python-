'''Write a Python program which asks the user to input a string. Perform the following
operations:
1.Slicing operation
2.Concatenate by using + and , operator'''

input = input("Enter a string: ")

# Slicing
print("Sliced string (1:6):", input[1:6])

# Concatenate using +
concat_string = input + " is awesome!"
print("Concatenated string using +:", concat_string)

# Concatenate using ,
print("Concatenated string using ,:", input, "is awesome!")
