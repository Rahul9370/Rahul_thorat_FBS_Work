class Student:
    def __init__(self, rno, name, sy, ty):
        self.rno = rno
        self.name = name
        self.sy = sy
        self.ty = ty
        self.grade = None   

    def add_marks(self):
        total = self.sy + self.ty   
        if total >= 70:
            self.grade = "A"
        elif total >= 60:
            self.grade = "B"
        elif total >= 50:
            self.grade = "C"
        elif total >= 40:
            self.grade = "Pass Class"
        else:
            self.grade = "Fail"

    def __str__(self):
        return (f"Roll No: {self.rno}, Name: {self.name}, "
                f"SY: {self.sy}, TY: {self.ty}, Grade: {self.grade}")



s1 = Student(1, "Rahul", 10, 10)
s1.add_marks()   # Calculate grade
print(s1)        # Display result
