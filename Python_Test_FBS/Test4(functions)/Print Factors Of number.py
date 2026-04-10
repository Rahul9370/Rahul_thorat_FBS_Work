# Write a function to which we pass a parameter and print the factors of a given number.
# for ex: 12=1,2,3,4,6,12

def Factors(num):
    for i in range(1,num+1):
        if(num%i==0):
         print(i)

num = int(input("Enter number to find Factors of given number :"))
Factors(num)