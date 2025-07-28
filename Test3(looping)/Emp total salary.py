# WAP to accept basic salary of n emp. (n should be accepte from user). If basic salary is below 20000 then
# da=10%, ta=12%, and hra=%15 otherwise da=15%, ta=18%, and hra=20%. Based on this calculate the total salary
# of each employee and and also total salary of all emp.

employee = int(input("Enter number of employee to calculate basic salary :"))
basic_salary = int(input("Enter basic salary of employee :"))
total = 0

if(basic_salary < 20000):
    for i in range(1,employee+1):
        total = total + (basic_salary*10)/100 + (basic_salary*12)/100 + (basic_salary*15)/100 + basic_salary
elif(basic_salary >= 20000):
    for i in range(1,employee+1):
        total = total + (basic_salary*15)/100 + (basic_salary*18)/100 + (basic_salary*20)/100 + basic_salary
else:
    print("Wrong Input!!!!!....")

print(total)