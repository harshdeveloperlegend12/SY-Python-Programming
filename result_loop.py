total = 0

for i in range(1, 6):
    marks = float(input("Enter marks for Subject: "))
    total += marks


percentage = (total / 500) * 100

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("\n----- Result -----")
print("Total Marks =", total)
print("Percentage =", round(percentage, 2), "%")
print("Grade =", grade)