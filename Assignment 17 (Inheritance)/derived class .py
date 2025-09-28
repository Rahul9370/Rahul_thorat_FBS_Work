"""2. Create a derived class from Student as EnggStudent with :
a. Data members as :
i. Branch
ii. InternalMarks
b. Add the following methods :
i. Parameterized constructor
ii. Display
iii. Accept
iv. override Method CalculateRank
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

class Enggstudent(Student):
    def __init__(self,sid=1,name="abc",age=18,per=80,branch="IT",imark=70):
        super().__init__(sid,name,age,per)
        self.branch = branch
        self.imark = imark

    def accept(self):
        super().accept()
        self.branch = input("Enter Student branch :")
        self.imark = int(input("Enter student internal marks :"))

    def display(self):
        super().display()
        print("Student branch name :",self.branch)
        print("Student internal marks :",self.imark) 

    def __str__(self):
        return f"""{super().__str__()} 
        student branch :{self.branch}\n student internal marks :{self.imark}"""

    def calRank(self):
        if(self.per >= 90 and self.per <=100):
            print("First rank")
        elif(self.per >= 70):
            print("Second Rank")
        elif(self.per >= 40):
            print("Third Rank")
        else:
            print("Fail or invalid input")


print("\n--- Engineering Student ---")
s2 = Enggstudent(102,"Amit",22,91,"CSE",85)
# s2.accept()
print(s2)
s2.display()
s2.calRank()
