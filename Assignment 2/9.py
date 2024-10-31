'''Write a program to create a dictionary with 5 items. Print dictionary items with its 
index '''

dict = {"apple": 1, "banana": 2, "cherry": 3, "date": 4, "elderberry": 5}

for i, (key, value) in enumerate(dict.items()):
    print(f"Index {i}: {key}")