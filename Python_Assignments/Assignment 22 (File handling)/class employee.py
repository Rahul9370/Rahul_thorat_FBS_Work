"""1. Create a class Emp (eid,ename,basic)
2. WAP a menu driven program to perform following operations using
files :

a. Add a record
b. Search for a record using id
c. Delete a record using id
d. Edit a record using id.
e. Display all records."""
class Emp:
    def __init__(self, eid=1, name="", salary=0):
        self.eid = eid
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"{self.eid},{self.name},{self.salary}\n"


    def addEmployee(self):
        id = int(input("enter user id :"))
        nm = input("Enter name :")
        sal = int(input("Enter salary :"))
        e = Emp(id,nm,sal)

        # f1 = open("data.txt", "a")
        # f1.write(str(e))
        # f1.close()

        with open("data.txt", "a") as f1:
            f1.write(str(e))

    def display(self):
        with open("data.txt", "r") as f1:
            for s in f1:
                print(s)

    def searchEmployee(self):
        id = int(input("Enter id :"))
        with open("data.txt", "r") as f1:
            for s in f1:
                list1 = s.split(",")
                # print(list1)
                if(list1[0] == str(id)):
                    print(s)
                    break
            else:
                print("Record not found")

    def updateEmployee(self):
        container = []
        found = False
        id = int(input("Enter id to update :"))
        with open("data.txt","r") as f1:
            for s in f1:
                list1 = s.split(",")
                if(list1[0] == str(id)): 
                    found = True                            # if record found
                    print("1.update name \n2.update salary")
                    ch = int(input("Enter option to update :"))
                    if(ch == 1):
                        nm = input("Enter new name :")
                        list1[1] = nm 
                    else:
                        sal = int(input("Enter new salary :"))
                        list1[2] = str(sal)
                    s = ",".join(list1)
                    container.append(s)
                else:                                                # if record not found
                    container.append(s)

        if(found == False):
            print("Record not found")
        else:
            # if record found then only process
            # open blank file for writing
            with open("data.txt","w") as f1:
                # from container put records back to file 
                for s in container:
                    f1.write(s)


    def deleteEmployee(self):
        container = []                                   # empty container for storing records
        found = False
        id = int(input("Enter id :"))
        with open("data.txt", "r") as f1:
            for s in f1:
                list1 = s.split(",")
                if(list1[0] != str(id)):     # if the record to be deleted not found put to container
                    container.append(s) 
                else:
                    found = True
        if(found == False):
            print("Id not found")  
        else:                                       # if record found then only process
            print("user deleted successfully")
            with open("data.txt", "w") as f1:          # open blank file for writing
                for c in container:                 # from container put records back to file
                    f1.write(c) 

c = Emp()

print("1. Admin")
print("2. User")

opt = int(input("Enter option :"))
if(opt == 1):
    uid = input("Enter user name :")
    pass1 = input("Enter password :")
    if(uid == "f" and pass1 == "1"):
        ch = 0
        while(ch != 6):
            print("1. Add employee")
            print("2. Display all employee")
            print("3. Search employee")
            print("4. Update employee")
            print("5. Delete employee")
            ch = int(input("Enter choise :"))
            if(ch == 1):
                c.addEmployee()
            elif(ch == 2):
                c.display()
            elif(ch == 3):
                c.searchEmployee()
            elif(ch == 4):
                c.updateEmployee()
            elif(ch == 5):
                c.deleteEmployee()