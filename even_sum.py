sum=0
print("Please enter 10 numbers:")

for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    
    if num % 2 == 0:
       sum+=num

print(f"The sum of even numbers is: ",sum)
