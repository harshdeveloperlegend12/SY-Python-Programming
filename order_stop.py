order_list=[]

print("--- Welcome to the Food Order System ---")
print("Enter the food items you want to order one by one.")
print("Type 'Stop' when you are finished.\n")

while True:
     item = input("Enter food item: ").strip()
    
    if item.lower() == "stop":
       			 break
        
     if item:
       			 order_list.append(item)
        		 print("Added",item,"to your order.")
    else:
       			 print("Please enter a valid food item.")

			 print("\n--- Your Final Order Summary ---")

   if order_list:
   				 for index, food in enumerate(order_list, start=1):
      				  print(index, food)
   else:
    				print("No items were ordered.")
