#6. WAP to calculate total salary of employee based on basic, da=10% of basic,ta=12% of basic, hra=15% of basic.

basic_salary = int(input("Enter basic salary of Employee:"))

da = 0.10 * basic_salary   # da(Dearness allowance)
ta = 0.12 * basic_salary    # ta(Travel allowance)
hra = 0.15 * basic_salary    # hra(House rent allowance)

total_salary = basic_salary + da + ta + hra

print("Total salary of Employee is:",total_salary)