"""13. Write a program to input electricity unit charges and calculate total electricity bill
according to the given condition:
For first 50 units Rs. 0.50/unit
For next 100 units Rs. 0.75/unit
For next 100 units Rs. 1.20/unit
For unit above 250 Rs. 1.50/unit
An additional surcharge of 20% is added to the bill
    bill = units * 0.5
    units = units - 50
    bill += units * 0.75"""

units = int(input("Enter electricity bill Units :"))

if(units <= 50):
    bill = units * 0.5                  #For first 50 units Rs. 0.50/unit
elif(units > 50 and units <= 150):
    bill = ((units * 0.5) + (units - 50) * 0.75)
    # bill = units * 0.5
    # units = units - 50
    # bill += units * 0.75                #For next 100 units Rs. 0.75/unit  
elif(units > 150 and units <= 250): 
    bill = (units * 0.5) + ((units - 50) * 0.75) + ((units - 150) * 1.20)
    # bill = units * 0.5
    # units = units - 50
    # bill += units * 0.75
    # units = units - 100
    # bill += units * 1.20                #For next 100 units Rs. 1.20/unit
else:
    bill = (units * 0.5) + ((units - 50) * 0.75) + ((units - 150) * 1.20) + (units - 250) * 1.50
    # bill = units * 0.5
    # units = units - 50
    # bill += units * 0.75
    # units = units - 100
    # bill += units * 1.20
    # units = units - 100
    # bill += units * 1.50                #For unit above 250 Rs. 1.50/unit


bill += bill * 0.20                               #An additional surcharge of 20% is added to the bill        
print("Total electricity bill is Rs:",bill)
