# 1. Write a program to prompt user to enter userid and password. If Id and
# password is incorrect give him chance to re-enter the credentials. Let him try 3
# times. After that program to terminate.

userid = input("Enter user id :")
password = input("Enter user password :")

for i in range(1 , 3+1):
    user_id = input("Enter your user id to login :")
    pass_word = input("Enter your password to login :")
    if(userid == user_id and password == pass_word):
        print("Login successfully...")
        break
    else:
        print("Incorrect user id or password")