"""1. A list contains the denominations as follows :
D = [2000, 500, 200, 100 , 50, 20, 10, 5]
Accept an amount from user and calculate how many
minimum number of notes will be needed for that
amount."""

def noteCal(mylist,amount):
    sum = 0
    for i in range(len(mylist)):
        if(amount >= 5):
            sum = sum + (amount // mylist[i])
            amount = amount % mylist[i]
    print("Total notes for given amount is :",sum)

mylist = [2000,500,200,100,50,20,10,5]
amount = int(input("Enter amount for calculate notes :"))
noteCal(mylist,amount)