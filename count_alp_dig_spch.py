string = input("Enter a string: ")

alphabets = 0
digits = 0
special_char = 0

for char in string:
    if char.isalpha():
        alphabets += 1
    elif char.isdigit():
        digits += 1
    else:
        special_char += 1
        
print("\nTotal Alphabets: ",alphabets)
print("Total Digits: ",digits)
print("Total Special Characters: ",special_char)
