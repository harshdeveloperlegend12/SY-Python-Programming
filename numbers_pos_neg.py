#Accept 10 numbers using for loop.
#Check each number if its positive , negative or zero.

for i in range(10):
 number= int(input("Enter the number: "))
 if number>0:
   print("Positive Number")
 elif number<0:
   print("Negative Number")
 else:
   print("Zero")