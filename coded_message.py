# Ask the user for the coded message and the secret message
coded_message = input("Enter the coded message: ")
secret_message = input("Enter the secret message: ")

# Clean inputs
coded_clean = coded_message.strip().lower()
secret_clean = secret_message.strip().lower()

# Reverse the secret message using Python slicing [::-1]
reversed_secret = secret_clean[::-1]

# Check using regular, backward, and missing conditions
if secret_clean == "":
    print("\nError: You did not enter a secret message.")
elif secret_clean in coded_clean:
    print(f"\nSuccess! Found standard message: '{secret_message}'")
elif reversed_secret in coded_clean:
    print(f"\nSuccess! Found backward spy message! '{secret_message}' was hidden as '{reversed_secret}'")
elif secret_clean not in coded_clean and reversed_secret not in coded_clean:
    print("\nAccess Denied: No hidden messages found.")

