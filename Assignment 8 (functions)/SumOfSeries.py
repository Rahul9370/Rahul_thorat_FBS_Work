#3. Write a program to find sum of following series using functions :
#a. 1+ 2 + 3 + 4+..... + n
#b. 1!+ 2! + 3! + 4!+..... + n!
#c. 1^1 + 2^2 + 3^3+ ...... n^n

# menu driven program
# without parametre without return value

# type - 1

#a. 1+ 2 + 3 + 4+..... + n
def SumOfSeries():
    num = int(input("Enter number to find sum of series till that number : "))
    sum = 0
    for i in range(1,num+1):
        sum = sum + i
    print("Sum of 1 to",num,"number is :",sum)


#b. 1!+ 2! + 3! + 4!+..... + n!
def SumOfFactorial():
    num = int(input("Enter number to find sum of factorial till that number : "))
    sum = 0
    for i in range(1,num+1):
        fact = 1
        for j in range(1,i+1):
            fact = fact * j
        sum = sum + fact
    print("Sum of 1 to",num,"factorial is :",sum)


#c. 1^1 + 2^2 + 3^3+ ...... n^n
def SumOfPower():
    num = int(input("Enter number to find sum of powers till that number : "))
    sum = 0
    for i in range(1,num+1):
        sum = sum + (i**i)
    print("Sum of 1 to",num,"number power is :",sum)


print("Choose operation number as per your requirement.")
print("option 1 is for to find sum of series upto n numbers.")
print("option 2 is for to find sum of factorial upto n numbers.")
print("option 3 is for to find sum of powers of upto n numbers.")
choise = int(input("Enter option number :"))
if(choise==1):
    SumOfSeries()
elif(choise==2):
    SumOfFactorial()
elif(choise==3):
    SumOfPower()
else:
    print("Invalid option...")



