# Taking user inputs
n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))

# Comparing the numbers
if n1>n2:
    print("The largest number is: ",n1)
elif n2 > n1:
    print("The largest number is: " ,n2)
else:
    print("Both numbers are equal.")
