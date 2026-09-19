count = 1

while (count <= 5):
    salary = float(input(f"Enter salary for Employee {count}: "))
    
    if salary < 30000:
        bonus = salary * 0.15
    elif salary <= 60000:
        bonus = salary * 0.10
    else:
        bonus = salary * 0.05
        
    final_salary = salary + bonus
    print("Bonus: ",bonus)
    print("Final Salary: ",final_salary)
    print("-" * 30)
    count=count+1
     
