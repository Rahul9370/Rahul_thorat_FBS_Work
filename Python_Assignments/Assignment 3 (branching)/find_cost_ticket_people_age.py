'''11. Accept age of five people and also per person ticket amount and then calculate total
amount to ticket to travel for all of them based on following condition :
a. Children below 12 = 30% discount
b. Senior citizen (above 59) = 50% discount
c. Others need to pay full.'''

age1 = int(input("Enter Age 1 people's :"))
age2 = int(input("Enter Age 2 people's :"))
age3 = int(input("Enter Age 3 people's :"))
age4 = int(input("Enter Age 4 people's :"))
age5 = int(input("Enter Age 5 people's :"))

amount = 100                               # per ticket amount is 100 rs.
total=0

if(age1 < 12):                     
    total += amount - (amount * 0.3)       # children below 12 age has = 30% discount
elif(age1 > 59):
    total += amount - (amount * 0.5)       # senior citizon above 59 age has = 50% discount
else:
    total += amount                        # 12 to 59 has need to pay full amount of ticket that is = 100

if(age2 < 12):                     
    total += amount - (amount * 0.3)       # below 12 age has 30% discount
elif(age2 > 59):
    total += amount - (amount * 0.5)       # above 59 age has 50% discount
else:
    total += amount                        # 12 to 59 has full amount of ticket that is 100

if(age3 < 12):                     
    total += amount - (amount * 0.3)       # below 12 age has 30% discount
elif(age3 > 59):
    total += amount - (amount * 0.5)       # above 59 age has 50% discount
else:
    total += amount                        # 12 to 59 has full amount of ticket that is 100

if(age4 < 12):                     
    total += amount - (amount * 0.3)       # below 12 age has 30% discount
elif(age4 > 59):
    total += amount - (amount * 0.5)       # above 59 age has 50% discount
else:
    total += amount                        # 12 to 59 has full amount of ticket that is 100

if(age5 < 12):                     
    total += amount - (amount * 0.3)       # below 12 age has 30% discount
elif(age5 > 59):
    total += amount - (amount * 0.5)       # above 59 age has 50% discount
else:
    total += amount                        # 12 to 59 has full amount of ticket that is 100

print("Total Amount of Tickets to Travel all ages People's is RS:",total)
