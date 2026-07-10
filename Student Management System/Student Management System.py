import os
import json

students = [
    {
    "id":101,
    "name":"Rahul",
    "age":19,
    "course":"Data Science",
    "marks":87
}
]

def check_id(a):
    for i in range(len(students)):
        if a==students[i]["id"]:
            return students[i]
    else:
        return False
    
file_path = r"D:\Python\Student Management System\Students.json"

def save_students():
    with open(file_path, "w") as file:
        for student in students:
            file.write(json.dumps(student))
            file.write("\n")

def load_students():
    with open(file_path, "r") as file:
            for line in file:
                if line.strip():
                    stud = json.loads(line)
                    students.append(stud)

def add_student():
    new = {}
    a = int(input("Enter ID: "))
    data = check_id(a)
    if data==False:
        new["id"] = a
        new["name"] = input("Enter Name: ")
        new["age"] = int(input("Enter Your Age: "))
        new["course"] = input("Enter Your Course: ")
        new["marks"] = int(input("Enter Marks: "))
        students.append(new)
        save_students()
        return f"Student Added Successfully"
    else:
        return "ID Already Exists"

def view_students():
    for student in students:
        print(student)
    
def search_student():
    a = int(input("Enter Student ID: "))
    data = check_id(a)
    if data!=False:
        return data
    else:
        return "No Student Found"
    
def update_student():
    a = int(input("Enter Student ID: "))
    data = check_id(a)
    if data!=False:
        print("""
Select What you Want to Update:
1. ID
2. Name
3. Age
4. Course
5. Marks
""")
        b = int(input("Your Option: "))
        if b==1:
            c = int(input("Enter Updated ID: "))
            check = check_id(c)
            if check==False:
                data["id"] = c
                save_students()
                return "ID Updated Successfully"
            else:
                return "ID Already Exists"
        elif b==2:
            c = input("Enter Updated Name: ")
            data["name"] = c
            save_students()
            return "Name Updated Successfully"
        elif b==3:
            c = int(input("Enter Updated Age: "))
            data["age"] = c
            save_students()
            return "Age Updated Successfully"
        elif b==4:
            c = input("Enter Updated Course: ")
            data["course"] = c
            save_students()
            return "Course Updated Successfully"
        elif b==5:
            c = int(input("Enter Updated Marks: "))
            data["marks"] = c
            save_students()
            return "Marks Updated Successfully"
        else:
            return "Please Select a Valid Option"
        
def delete_student():
    a = int(input("Enter Student ID: "))
    data = check_id(a)
    if data!=False:
        for i in range(len(students)):
            if students[i]["id"]==data["id"]:
                students.pop(i)
                save_students()
                return f"Deleted Successfully"
    else:
        return f"No Student With {a} ID"

def show_topper():
    maxi = 0
    for student in students:
        if student["marks"]>maxi:
            maxi = student["marks"]
    for student in students:
        if student["marks"]==maxi:
            return f"Topper is {student["name"]} with {maxi} Marks"

def calculate_average():
    suma = 0
    count = 0
    for student in students:
        suma += student["marks"]
        count += 1
    avg = suma/count
    return f"Average is {avg}"
    
def main():
    running = True
    load_students()

    while (running!=False):

        print("""
Select From Following: 
1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Show Topper
7. Calculate Average Marks
8. Exit
""")
        
        a = int(input("Enter Your Selection: "))
        
        if a==1:
            print(add_student())
            running = True
        elif a==2:
            view_students()
            running = True
        elif a==3:
            print(search_student())
            running = True
        elif a==4:
            print(update_student())
            running = True
        elif a==5:
            print(delete_student())
            running = True
        elif a==6:
            print(show_topper())
            running = True
        elif a==7:
            print(calculate_average())
            running = True
        elif a==8:
            running = False
        else:
            return f"Please Select From Given Options"
        
main()