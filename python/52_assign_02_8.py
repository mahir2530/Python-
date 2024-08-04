lst = [True, False ,True , True]

all_true = all(lst)

any_true = any(lst)

enumerated_list = list(enumerate(lst))

print("All Element True : ", all_true)
print("Any Element True : ", any_true)
print("Enumersted List : ")

for index, value in enumerated_list:
    print(f"[index of {index}] : [value is {value}]")