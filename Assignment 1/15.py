'''Write a Python program that will perform following conversions using appropriate
method:
1. string to integer
2. integer to float
3. tuple to list
4. string to list
5. list to tuple'''

# String to integer
string = "123"
int_ = int(string)
print("String to integer:", int_)

# Integer to float
int_ = 123
float_ = float(int_)
print("Integer to float:", float_)

# Tuple to list
tuple_ = (1, 2, 3)
list_ = list(tuple_)
print("Tuple to list:", list_)

# String to list
string_ = "Hello"
list_ = list(string_)
print("String to list:", list_)

# List to tuple
list_ = [1, 2, 3]
tuple_ = tuple(list_)
print("List to tuple:", tuple_)
