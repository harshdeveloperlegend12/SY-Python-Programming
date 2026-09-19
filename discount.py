bill = int(input("Enter the bill amount: ")) 

if (bill >= 5000):
    final_bill = bill * 0.60
else:
    final_bill = bill

print("Final Bill Amount: ₹", final_bill)
