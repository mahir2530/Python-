dict1 = {
    "Rohan" : 1,
    "Adi" : 2,
    "Ishan" : 3,
    "Yash" : 4,
    "Jay" : 5
}

copy = dict1.copy()
print("\nCopied Dictionary : ", copy)

dict1["Jay"] = 6
print("\nUpdated Dictionary : ", dict1)

find_key = "Yash"
if find_key in dict1:
    value = dict1[find_key]
    print(f"\nvalue of '{find_key}' : ", value)

else:
    print(f"\n{find_key} is not found in Dictionary")

