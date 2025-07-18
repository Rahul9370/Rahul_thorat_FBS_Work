"""5. Write a program to accept an integer amount from user and tell minimum
number of notes needed for representing that amount. (Use looping to optimize
the problem)"""

amount = int(input("Enter total amount to distribute in minimum notes :"))

note500 = amount // 500
re_amount = amount % 500
print(re_amount)
note200 = re_amount // 200
re_amount %=  200                  # we can assign directle re_amount variable like this 

note100 = re_amount // 100
re_amount = re_amount % 100

note50 = re_amount // 50
re_amount = re_amount % 50

note20 = re_amount // 20
re_amount = re_amount % 20

note10 = re_amount // 10
re_amount = re_amount % 10

print("notes for 500:",note500)
print("notes for 200:",note200)
print("notes for 100:",note100)
print("notes for 50:",note50)
print("notes for 20:",note20)
print("notes for 10:",note10)

total_note = note500 + note200 + note100 + note50 + note20 + note10        #cal total notes needed for given amount

print("Minimum number of notes needed for representing that amount is:",total_note)
    