def cal_discount(bill):
    bill = float(bill)
    discount = bill * 10 / 100
    final_amount = bill - discount

    print("Bill Amount:", bill)
    print("Discount (10%):", discount)
    print("Final Amount:", final_amount)

bill_amount = input("Enter bill amount: ")
cal_discount(bill_amount)