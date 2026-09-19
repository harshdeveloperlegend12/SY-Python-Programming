#count positive number from a list
num=[3,6,8,-1,-4,9,-2]
count=0
for i in num:
	if i>0:
		count=count+1
print("Count of positive numbers is:",count)