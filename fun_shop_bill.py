def shop_bill(item1, item2, item3):
  total = item1 + item2 + item3
  return total

a =float(input("Enter the value of item1: "))
b =float(input("Enter the value of item2: "))
c =float(input("Enter the value of item3: "))

total_bill = shop_bill(a,b,c)
print("The total shopping bill is:", total_bill)
