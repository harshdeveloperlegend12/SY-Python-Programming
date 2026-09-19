user_input = input("Enter the file name: ")

if user_input.lower().endswith(".pdf"):
    print("Yes, it is a PDF file.")
else:
    print("No, it is not a PDF file.")
