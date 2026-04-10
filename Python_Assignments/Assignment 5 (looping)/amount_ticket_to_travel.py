"""3. Accept no. of passengers from user and per ticket cost. Then accept age of each
passenger and then calculate total amount to ticket to travel for all of them based on
following condition :
a. Children below 12 = 30% discount
b. Senior citizen (above 59) = 50% discount
c. Others need to pay full."""

passengers = int(input("Enter number of passengers : "))
ticket_cost = int(input("Enter per ticket cost  : "))
total = 0

while(passengers > 0):
    age = int(input("Enter age of passenger : "))
    passengers -= 1
    if(age < 12):
        total = total + ticket_cost - (ticket_cost * 0.3)
    elif(age > 59):
        total = total + ticket_cost - (ticket_cost * 0.5)
    else:
        total = total + ticket_cost 

print("Total amount to travel is Rs.",total)
