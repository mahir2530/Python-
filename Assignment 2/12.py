'''Write a program which will show the following operations on Dictionary: 
• Copy dictionary 
• Update an item in dictionary 
• Return the value of given key '''
dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}


copy_d = dict.copy()
print("Copied Dictionary:", copy_d)

k = 'age'
new_v = 26
dict[k] = new_v
print("Updated Dictionary:", dict)

key_to_lookup = 'city'
value = dict.get(key_to_lookup)
print(f"The value for the key '{key_to_lookup}' is:", value)
