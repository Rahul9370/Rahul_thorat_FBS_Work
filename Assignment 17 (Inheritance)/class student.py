"""1. Create a class Student with following
a. data members :
i. StudentId
ii. Name
iii. Age
iv. Percentage
b. Add the following methods :
i. Parameterized constructor
ii. Display
iii. Accept
iv. Method CalculateRank
v. Override __str__ Method"""

class Student:
    def __init__(self,sid=1,name="abc",age=18,per=80):
        self.sid = sid
        self.name = name
        self.age = age
        self.per = per

    def accept(self):
        self.sid = int(input("Enter student id :"))
        self.name = input("Enter Student name :")
        self.age = int(input("Enter student age :"))
        self.per = float(input("Enter student percentage :"))

    def display(self):
        print("Student     id :",self.sid)
        print("Student   name :",self.name)
        print("Student    age :",self.age)  
        print("Student    per :",self.per)  

    def __str__(self):
        return f" student id :{self.sid}\n student name :{self.name}\n student age :{self.age}\n student percentage :{self.per}"

    def calRank(self):
        if(self.per >= 90 and self.per <=100):
            print("First rank")
        elif(self.per >= 70):
            print("Second Rank")
        elif(self.per >= 40):
            print("Third Rank")
        else:
            print("Fail or invalid input")

s1 = Student(101,"Rahul",23,82.40)
# print(s1)
s1.accept()
s1.display()
s1.calRank()
