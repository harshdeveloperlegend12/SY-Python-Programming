# Choose the number you want the factorial for (e.g., 5!)
n=int(input("Enter the value: "))
factorial = 1

# Loop from 1 up to (num + 1) because range excludes the last number
for i in range(1, n+1):
    factorial = factorial + i

print("The factorial of",n,"is: ",factorial)
