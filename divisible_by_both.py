num = int(input("Enter a number: "))

if (num % 3 == 0) & (num % 5 == 0):
    print(num,"is divisible by both 3 and 5.")
else:
    print(num," is NOT divisible by both 3 and 5.")
