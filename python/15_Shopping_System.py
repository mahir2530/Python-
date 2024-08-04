c_name = input("Enter Your Name : ")
p_name = input("Enter The Product Name : ")
price = int(input("Enter The Price : "))
qty = int(input("Enter The Product Quantity : "))

print("\n\n\n***** Welcome To Shopping *****")
print("Customer Name : ",c_name)
print("Product Name : ",p_name )
print("Price  : ",price)
print("Quantity : ",qty)

total = price * qty
print("Total : ",total)

if total >= 1500:
    disc = (total * 15) / 100
elif total>=1000:
    disc = (total * 10) / 100
elif total >=500:
    disc = (total * 5) / 100
elif total >= 0:
    disc = 0

net = total - disc
print("Net Total : ",net) 