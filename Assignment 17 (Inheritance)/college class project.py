"""4. Create a class College which has collection of students. Add the
following methods :
a. Parameteried constructor for number of students.
b. AddStudent
c. GetStudent
d. RemoveStudent
e. Override __str__ Method"""

class Student:
    def __init__(self, sid=1, name="abc", age=18, per=80):
        self.sid = sid
        self.name = name
        self.age = age
        self.per = per

    def accept(self):
        self.sid = int(input("Enter student id : "))
        self.name = input("Enter student name : ")
        self.age = int(input("Enter student age : "))
        self.per = float(input("Enter student percentage : "))

    def display(self):
        print(f"ID: {self.sid}, Name: {self.name}, Age: {self.age}, Percentage: {self.per}")

    def __str__(self):
        return f"ID: {self.sid}, Name: {self.name}, Age: {self.age}, Percentage: {self.per}"

    def calRank(self):
        if 90 <= self.per <= 100:
            return "First rank"
        elif 70 <= self.per < 90:
            return "Second rank"
        elif 40 <= self.per < 70:
            return "Third rank"
        else:
            return "Fail"

class EnggStudent(Student):
    def __init__(self, sid=1, name="abc", age=18, per=80, branch="IT", imark=70):
        super().__init__(sid, name, age, per)
        self.branch = branch
        self.imark = imark

    def accept(self):
        super().accept()
        self.branch = input("Enter branch : ")
        self.imark = int(input("Enter internal marks : "))

    def display(self):
        super().display()
        print(f"Branch: {self.branch}, Internal Marks: {self.imark}")

    def __str__(self):
        return f"{super().__str__()}, Branch: {self.branch}, Internal Marks: {self.imark}"

class MedicalStudent(Student):
    def __init__(self, sid=1, name="abc", age=18, per=80, specialization="General", imark=70):
        super().__init__(sid, name, age, per)
        self.specialization = specialization
        self.imark = imark

    def accept(self):
        super().accept()
        self.specialization = input("Enter specialization : ")
        self.imark = int(input("Enter internship marks : "))

    def display(self):
        super().display()
        print(f"Specialization: {self.specialization}, Internship Marks: {self.imark}")

    def __str__(self):
        return f"{super().__str__()}, Specialization: {self.specialization}, Internship Marks: {self.imark}"

class College:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.students = []

    def addStudent(self, student):
        if len(self.students) < self.capacity:
            self.students.append(student)
            print(f"Student {student.name} added.")
        else:
            print("Cannot add student: College is full.")

    def getStudent(self, sid):
        for s in self.students:
            if s.sid == sid:
                return s
        return None

    def removeStudent(self, sid):
        original_count = len(self.students)
        self.students = [s for s in self.students if s.sid != sid]
        if len(self.students) < original_count:
            print(f"Student with ID {sid} removed.")
        else:
            print(f"No student found with ID {sid}.")

    def __str__(self):
        result = "College Students:\n"
        for s in self.students:
            result += str(s) + "\n"
        return result

c = College(5)

s1 = Student(101, "Rahul", 23, 82)
s2 = EnggStudent(102, "Amit", 22, 91, "CSE", 85)
s3 = MedicalStudent(103, "Sonia", 21, 88, "Dentist", 90)

c.addStudent(s1)
c.addStudent(s2)
c.addStudent(s3)

print("\n--- College Student List ---")
print(c)

print("\n--- Get Student ID 102 ---")
student = c.getStudent(102)
if student:
    student.display()
    print("Rank:", student.calRank())

print("\n--- Remove Student ID 101 ---")
c.removeStudent(101)
print(c)
