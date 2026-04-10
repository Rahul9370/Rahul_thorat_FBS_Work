# 10. Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)

male_age = int(input("Enter Age of Male :"))
female_age = int(input("Enter Age of Female :"))

if(male_age >= 21 and female_age >= 18):
    print("Both male and female is eligible to Marry!!!")
else:
    print("Not Eligible for Marry...")