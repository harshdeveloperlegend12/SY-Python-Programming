'''COUSTMER ENTER COUPEN CODE IGNORE UPPER AND LOWER, CHECK WHETHER IT MATCHES TO STORE COUPEN CODE OR NOT'''

STORE_COUPON = "SUMMER50"

user_coupon = input("Enter your coupon code: ")

if user_coupon == STORE_COUPON.lower():
    print("Success! Coupon applied successfully.")
else:
    print("Invalid coupon code. Please try again.")
