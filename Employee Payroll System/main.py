from Work import Employee_Work

def main():
    ongoing = True
    emp = Employee_Work()
    emp.Load_Employee()
    while ongoing:
        print("""Select from Following: 
1. Add Employee
2. View Employees
3. Search Employee
4. Update Employee
5. Delete Employee
6. Calculate Salary
7. Save Data
8. Load Data
9. Exit""")
        try:
            a = int(input("Enter Your Choice: "))
            if a == 1:
                emp.Add_Employee()
            elif a==2:
                emp.View_Employees()
            elif a==3:
                emp.Search_Employee()
            elif a == 4:
                emp.Update_Employee()
            elif a==5:
                emp.Delete_Employee()
            elif a==6:
                emp.Calculate_Salary()
            elif a==7:
                emp.Save_Employees()
            elif a==8:
                emp.Load_Employee()
            elif a==9:
                ongoing = False
            else:
                print("Please Select From Given Options")
        except ValueError:
            print("Enter numbers only")
            ongoing = True

main()