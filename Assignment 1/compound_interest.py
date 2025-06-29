# 4) WAP to cal compound interest

principle = int(input("Enter principle:"))
years = int(input("Enetr no. of years:"))
rate = float(input("Enter rate of interest:"))

compound_interest = principle*(1+(rate/100))**years

print("Compound interest of given data:",compound_interest)

