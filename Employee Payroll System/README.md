# Employee Payroll System

A console-based **Employee Payroll Management System** built using Python. This project demonstrates Object-Oriented Programming concepts such as inheritance, polymorphism, encapsulation, file handling, and JSON data storage.

The system allows users to manage full-time and part-time employees, calculate salaries, and store employee records permanently using JSON files.

---

## 🚀 Features

- Add new employees
- View all employees
- Search employees by ID
- Update employee details
- Delete employees
- Calculate employee salary
- Save employee data into JSON file
- Load employee data from JSON file
- Separate handling for Full-Time and Part-Time employees
- Input validation using exception handling

---

## 🛠️ Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- JSON File Handling
- Exception Handling

---

## 📂 Project Structure

```
Employee Payroll System/
│
├── main.py                 # Program execution and menu system
├── Work.py                 # Employee management operations
├── Employee_Time.py        # Employee classes and salary logic
├── Employees.json          # Stores employee records
└── README.md               # Project documentation
```

---

## 🧠 OOP Concepts Implemented

### Inheritance
The project uses inheritance where different employee types inherit common properties from the base Employee class.

```
Employee
    |
    ├── FullTimeEmployee
    |
    └── PartTimeEmployee
```

### Polymorphism
Both employee types implement their own salary calculation logic using the same method:

```python
calculate_salary()
```

### Encapsulation
Employee data is managed through classes and objects instead of directly modifying data structures.

---

## 👨‍💼 Employee Types

### Full-Time Employee

Salary calculation:

```
Salary = Monthly Salary
```

Example:

```
Employee:
Name: Rahul
Type: Full Time
Salary: 50000
```

---

### Part-Time Employee

Salary calculation:

```
Salary = Hourly Rate × Hours Worked
```

Example:

```
Employee:
Name: Amit
Type: Part Time
Hourly Rate: 200
Hours Worked: 80

Salary = 200 × 80 = 16000
```

---

## ▶️ How to Run

1. Clone the repository

```bash
git clone <repository-url>
```

2. Navigate to the project directory

```bash
cd Employee-Payroll-System
```

3. Run the program

```bash
python main.py
```

---

## 📋 Menu Options

```
1. Add Employee
2. View Employees
3. Search Employee
4. Update Employee
5. Delete Employee
6. Calculate Salary
7. Save Data
8. Load Data
9. Exit
```

---

## 💾 Data Storage

Employee records are stored in:

```
Employees.json
```

Example:

```json
[
    {
        "employee_id": 101,
        "name": "Rahul",
        "department": "IT",
        "type": "Full Time",
        "salary": 50000
    }
]
```

---

## 🎯 Learning Outcomes

Through this project, I practiced:

- Designing classes and objects
- Implementing inheritance
- Understanding polymorphism
- Working with JSON files
- Building CRUD operations
- Handling user input errors
- Structuring Python projects into multiple files

---

## 🔮 Future Improvements

Possible improvements:

- Add login authentication
- Add database support using SQLite/MySQL
- Generate salary slips as PDF
- Add graphical user interface using Tkinter
- Add attendance management
- Add employee performance tracking

---

## 👨‍💻 Author

**Sanjay Ladumor**

GitHub: https://github.com/SanjayLadumor