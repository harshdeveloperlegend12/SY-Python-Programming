'''
car=['BMW','BENZ','ROLLS ROYCE','JAGUAR','DEFENDER']
car.append("RANGE ROVER")
print(car)

#EXTEND()
car=['BMW','BENZ','ROLLS ROYCE','JAGUAR','DEFENDER']
car.extend(["RANGE ROVER","LAMBORGINI","FERRARI"])
print(car)

#INSERT()
car=['BMW','BENZ','ROLLS ROYCE','JAGUAR','DEFENDER']
car.insert(5,"KIA")
print(car)


#modify value
list=["Physics","Psychology",2000]
list[2]=2001
print("New value is: ",list[2])
'''
'''
a=len([1,2,3])
print(a)'''
'''
a=['hi','Welcome']*4
print(a)'''
'''
n=4 not in [1,2,3]
print(n)'''
'''
subjects=('MATHS','PSYCHOLOGY',5.6,7,7,7,7,'PSYCHOLOGY','PSYCHOLOGY','PSYCHOLOGY')
print(subjects.count('PSYCHOLOGY'))

print( subjects)
del subjects
print( subjects)'''

assign=['poster','PPT','PROTOTYPE']
assign.append("PROJECT")
assign.remove("PPT")
print(assign)
