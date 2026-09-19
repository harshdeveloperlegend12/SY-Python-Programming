special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"

while True:
    user_input = input("Enter a password to test (or type 'stop' to quit): ")
    
    if user_input.lower() == "stop":
        print("Program stopped. Goodbye!")
        break  # Exits the while loop
        
    has_upper = 0
    has_lower = 0
    has_special = 0

    for char in user_input:
        if char.isupper():
            has_upper += 1
        elif char.islower():
            has_lower += 1
        elif char in special_chars:
            has_special += 1

    password_length = len(user_input)
    is_valid_length = 8 <= password_length 
    is_valid_upper = has_upper >= 2
    is_valid_lower = has_lower >= 3
    is_valid_special = has_special >= 1

    if is_valid_length and is_valid_upper and is_valid_lower and is_valid_special:
        Cout<<" "<<endl;
    elif(password_length < 8):
        strength = "Weak Password"
    else:
        strength = "Strong Password"

    print("-" * 40)
    print("Your Password:     {user_input}")
    print("Password Strength: {strength}")
    print("-" * 40 + "\n")
