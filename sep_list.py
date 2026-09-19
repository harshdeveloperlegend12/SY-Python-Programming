even_numbers = []
odd_numbers = []

print("Please enter 10 numbers:")
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

print("\n--- Results ---")
print("Even numbers list:", even_numbers)
print("Odd numbers list:", odd_numbers)
