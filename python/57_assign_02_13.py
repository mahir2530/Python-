tup = [10, 20, 30, 40, 50]

replicate_tuple = tup * 4
print("Replicate Tuple : ", replicate_tuple)

slicing_tuple = tup[1:4]
print("Slicing Tuple : ", slicing_tuple)

def serached_tuple(t,item):
     try :
         index = t.index(item)
         return index
     except ValueError:
        return -1
    
     

item_to_search = 10
index_of_item = serached_tuple(tup, item_to_search)
if index_of_item != -1:
    print(f"Item {item_to_search} found at index {index_of_item}")
else:
    print(f"Item {item_to_search} not found in the tuple")