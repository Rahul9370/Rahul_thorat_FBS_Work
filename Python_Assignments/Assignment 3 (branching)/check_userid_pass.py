"""8. Write a program to prompt user to enter userid and password. After verifying
userid and password display a 4 digit random number and ask user to enter the
same. If user enters the same number then show him success message otherwise
failed. (Something like captcha)"""

import random

user_id = input("Enter user id :")
user_password = input("Enter user password :")
 

if(user_id == 'rahul' and user_password == '123'):
    captcha = random.randint(1111,9999)
    print("Your Captcha :",captcha)
    user_captcha = int(input("Enter Captcha :"))
    if(captcha == user_captcha):
        print("Login Successful..!")
    else:
        print("Captcha incorrect..!")
else:
    print("Incorrect user id or password. Login Failed..!")

