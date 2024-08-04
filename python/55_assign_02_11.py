dict1 = {
    "Rohan" : 1,
    "Adi" : 2,
    "Ishan" : 3,
    "Yash" : 4,
    "Jay" : 5
}

dict2 = {
    "apple": 1,
    "banana": 2,
    "olive": 3,
    "orange": 4
}

if "olive" in dict2:
    del dict2["olive"]
    print("\nDleted 1 item in dictionary : ",  dict2)

else:
    print("\nOlive not Found in Dict2")

if dict1 == dict2:
     print("\nDictionary 1 and Dictionary 2 are equal")

else:
     print("\nDictionary 1 and Dictionary 2 are not equal")

dict1.clear()
print("\nRemoving Item : ", dict1)