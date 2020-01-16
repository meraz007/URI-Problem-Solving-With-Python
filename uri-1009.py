sellers_name=str(input())

fixed_salary=float(input())
bonus=float(input())

per_bonus = bonus*.15

total_salary=fixed_salary+per_bonus

print("TOTAL = R$ %.2f"%total_salary)