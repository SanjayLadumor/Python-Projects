from Employee_Time import Employee, FullTimeEmployee, PartTimeEmployee
import os
import json

class Employee_Work:

    def __init__(self):
        self.employees = []
        self.current_employee = None
        self.file_path = os.path.join(os.path.dirname(__file__), "Employees.json")

    def Add_Employee(self):
        try:
            a = int(input("Enter Employee ID: "))
            if self.Find_Employee(a):
                print("Employee Already Exists")
                return
            else:
                name = input("Enter Name: ")
                department = input("Enter Department: ")
                emp_type = input("Employee Type(Full Time/Part Time): ")
                if emp_type == "Full Time":
                    salary = int(input("Enter Monthly Salary: "))
                    new_employee = FullTimeEmployee(
                        a,
                        name,
                        department,
                        salary
                    )
                elif emp_type == "Part Time":
                    rate = int(input("Enter Hourly Rate: "))
                    hours = int(input("Enter Hours Worked: "))
                    new_employee = PartTimeEmployee(
                        a,
                        name,
                        department,
                        rate,
                        hours
                    )
                else:
                    print("Invalid Employee Type")
                    return
                self.employees.append(new_employee)
                self.Save_Employees()
        except ValueError:
            print("Enter numbers only")
            return

    def View_Employees(self):
        for employee in self.employees:
            print(employee)

    def Find_Employee(self,employee_id):
        for employee in self.employees:
            if employee.employee_id == employee_id:
                return employee
        else:
            return None

    def Search_Employee(self):
        try:
            a = int(input("Enter Employee ID: "))
            data = self.Find_Employee(a)
            if data==None:
                print("No Employee Found")
            else:
                print(data)
        except ValueError:
            print("Enter numbers only")
            return

    def Load_Employee(self):
        with open(self.file_path,"r") as f:
            data = json.load(f)
            for employee in data:
                if employee["type"] == "Full Time":
                    new_emp = FullTimeEmployee(employee["employee_id"],employee["name"],employee["department"],employee["salary"])
                    self.employees.append(new_emp)
                else:
                    new_emp = PartTimeEmployee(employee["employee_id"],employee["name"],employee["department"],employee["hour_rate"],employee["hours_worked"])
                    self.employees.append(new_emp)

    def Save_Employees(self):
        data = []

        for employee in self.employees:
            data.append(employee.to_dict())

        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4)

        print("Employees Saved Successfully")

    def Update_Employee(self):
        try:
            a = int(input("Enter Employee ID: "))
            data = self.Find_Employee(a)
            if data==None:
                print("No Employee Found")
            else:
                print("""Select What you Want to Update: 
    1. Employee ID
    2. Name
    3. Department
    4. Type
    5. Calculate Salary
    6. Exit""")
                try:
                    b = int(input("Enter Your Choice: "))
                    if b == 1:
                        try:
                            c = int(input("Enter New Employee ID: "))
                            check = self.Find_Employee(c)
                            if check==None:
                                data.employee_id = c
                            else:
                                print("ID Already Exists")
                                return
                        except ValueError:
                            print("Enter numbers only")
                            return
                    elif b == 2:
                        c = input("Enter New Name: ")
                        data.name = c
                    elif b == 3:
                        c = input("Enter New Department: ")
                        data.department = c
                    elif b == 4:
                        c = input("Enter New Type: ")
                        if c == data.type :
                            print(f"Alreay of {c}")
                        else:
                            data.type = c
                            if data.type == "Full Time":
                                f = input("Enter Salary: ")
                                new_emp = FullTimeEmployee(
                                    data.employee_id,
                                    data.name,
                                    data.department,
                                    f
                                )
                                index = self.employees.index(data)
                                self.employees[index] = new_emp
                            else: 
                                rate = int(input("Enter Rate per Hour: "))
                                hours = int(input("Enter Hours Worked: "))
                                new_emp = PartTimeEmployee(
                                    data.employee_id,
                                    data.name,
                                    data.department,
                                    rate,
                                    hours
                                )
                                index = self.employees.index(data)
                                self.employees[index] = new_emp
                    elif b == 5:
                        try:
                            a = int(input("Enter Employee ID: "))
                            employee = self.Find_Employee(a)

                            if employee:
                                print(employee.calculate_salary())
                            else:
                                print("Employee Not Found")
                        except ValueError:
                            print("Enter numbers only")
                            return
                    elif b == 6:
                        return
                    else:
                        print("Please Select From Given Options")
                except ValueError:
                    print("Enter numbers only")
                    return
        except ValueError:
            print("Enter numbers only")
            return
        
    def Delete_Employee(self):
        a = int(input("Enter Employee ID: "))
        data = self.Find_Employee(a)
        if data==None:
            print("No Employee Found")
        else:
            self.employees.remove(data)
            print("Employee Deleted Successfully")

    def Calculate_Salary(self):
        try:
            a = int(input("Enter Employee ID: "))
            emp = self.Find_Employee(a)
            if emp:
                print(emp.calculate_salary())
            else:
                print("No Employee Found")
        except:
            print("Please Enter Number")
            return