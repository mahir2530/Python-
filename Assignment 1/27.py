'''Write a Python program which asks the user to input a string. Find the sub-string in given
string. (Hint: Welcome in GLS University, Find the position of ‘Uni’ from given string)'''

string = input("Enter a string: ")
substring = input("Enter the substring to find: ")
position = string.find(substring)
print("Position of substring:", position)
