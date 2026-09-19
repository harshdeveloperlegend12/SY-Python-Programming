#Constants Identifiers

Earth_Gravity= 9.8
Moon_Gravity = (1/6)*9.8

# User-defined function

def calculate_weight(mass, gravity):
    return mass*gravity

#main
#data type is float
#parameters are mass and gravity
#Arithmetic Operator is *

mass=float(input("Enter the mass of the object in Kg: "))
earth_weight= calculate_weight(mass, Earth_Gravity)
moon_weight= calculate_weight(mass, Moon_Gravity)

print("Weight on Earth: ",earth_weight, "N", type(mass))
print("Weight on Moon: ",moon_weight, "N", type(mass))