# WAP a program to cal Simple interest   based on Principle, Rate and Time (SI=P*R*T/100)

principle = int(input("Enter Principle amount:"))
rate = float(input("Enter Rate of interest:"))
years = int(input("Enter Yesrs:"));


simple_interest = (principle*rate*years)/100

print("Simple Interest:",simple_interest)