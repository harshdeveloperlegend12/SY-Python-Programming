text = "A man a plan a canal Panama"
reversed_code = text[::-1]

cleaned_text = text.replace(" ","").lower()
reversed_clean = cleaned_text[::-1]
is_palindrome = cleaned_text == reversed_clean

print("Secret Code:", reversed_code)
print("Is Palindrome?:", is_palindrome)
