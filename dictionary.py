students={}
name=input("Enter the student's name: ")
div=input("Enter the student's div: ")
students["student name"]=name
students["Division"]=div
print(students)

'''UPDATE'''

students.update({
"Enrolment No": "12345",
"Age": "20"
})
print(students)