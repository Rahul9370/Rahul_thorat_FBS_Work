# 7. Write a program to check if user has entered correct userid and password.

userid = input("Enter User id :")
password = input("Enter password :")

if(userid == 'rahul' and password == '123'):
    print("User login successfully !")
else:
    print("Incorrect user id or password !")