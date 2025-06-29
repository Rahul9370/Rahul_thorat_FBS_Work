# 3) Find simple interest

principle = int(input("Enter Principle amount:"))
years = int(input("Enter Yesrs:"));
rate = float(input("Enter Rate of interest:"))

simple_interest = (principle*years*rate)/100

print("Simple Interest:",simple_interest)