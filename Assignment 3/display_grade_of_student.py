# 9. Input 5 subject marks from user and display grade(eg.First class,Second class ..)

percentage = int(input("Enter Obtained Percentage :"))

if(percentage >= 80 and percentage <= 100):
    print("First Class...")
elif(percentage >= 70 and percentage <= 100):
    print("Second Class...")
elif(percentage >= 60 and percentage <= 100):
    print("Third Class...")
elif(percentage >= 40 and percentage <= 100):
    print("Fourth Class...")
elif(percentage > 100):
    print("Enter percentage between 1 to 100 only!!!")
else:
    print("Fail.....!")
