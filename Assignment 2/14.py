'''Create a list [“RED”, “BLUE”, “GREEN”] and perform following operations on it: 
• append an item “BLACK” in it 
• extend it adding a list [2,3,4] 
• Sort all the elements'''

l1 = ['RED', 'BLUE', 'GREEN']

l1.append("BLACK")
print("Appended list:", l1)

l1.extend(['WHITE', 'YELLOW', 'ORANGE']) 
print("Extended list:", l1)

l1.sort()
print("Sorted list of strings:", l1)

