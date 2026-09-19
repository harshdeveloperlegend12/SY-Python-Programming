def cal_calories(carbs, fats, proteins):
    calories = (carbs * 4) + (fats * 9) + (proteins * 4)
    return calories

carbs = float(input("Enter grams of carbohydrates: "))
fats = float(input("Enter grams of fats: "))
proteins = float(input("Enter grams of proteins: "))

total = cal_calories(carbs, fats, proteins)

print("Total Caloric Intake:", total, "calories")