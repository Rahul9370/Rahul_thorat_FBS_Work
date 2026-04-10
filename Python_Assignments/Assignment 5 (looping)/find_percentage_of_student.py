# 2. Enter number of students from user. For those many students accept marks of 5
# subject marks from user and calculate percentage. Display all percentage and
# average percentage of students.

students = int(input("Enter number of Students :"))
total_students = students
total_marks = int(input("Enter total marks of 5 subjects :"))
total_percentage = 0

while(students > 0):
    sub1 = int(input("Enter marks of sunject 1 :"))
    sub2 = int(input("Enter marks of sunject 2 :"))
    sub3 = int(input("Enter marks of sunject 3 :"))
    sub4 = int(input("Enter marks of sunject 4 :"))
    sub5 = int(input("Enter marks of sunject 5 :"))

    percentage = ((sub1 + sub2 + sub3 + sub4 + sub5) * 100) / total_marks
    total_percentage += percentage 
    print("Percentage of student ",students," is :",percentage,"%")
    students -= 1

average_percentage = total_percentage / total_students
print("Total percentage of ",total_students," students is :",total_percentage,"%")
print("Average percentage of ",total_students," students is :",average_percentage,"%")