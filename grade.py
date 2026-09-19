'''if marks fall btw 60-70 ( C), 70 - 80(B), 80-90(A), 90+(A+)
take user inputs of 5 diff subjects , calculate grade , percentage, '''

#Take inputs for 5 different subjects

s1 = float(input("Enter marks for Subject 1: "))
s2 = float(input("Enter marks for Subject 2: "))
s3 = float(input("Enter marks for Subject 3: "))
s4 = float(input("Enter marks for Subject 4: "))
s5 = float(input("Enter marks for Subject 5: "))

#Calculate total and percentage

tot_marks = s1 + s2 + s3 + s4 + s5
percentage = (tot_marks / 500) * 100

#Determine grade using if-elif-else

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
else:
    grade = "Fail"

#Print the final results
print("\n--- Results ---")
print("Total Marks:", tot_marks)
print("Percentage:", percentage, "%")
print("Grade:", grade)
