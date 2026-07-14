class Employee:

    def __init__(self,employee_id,name,department,type):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.type = type

    def calculate_salary(self):
        pass

    def __str__(self):
        return f"""
    ID: {self.employee_id}
    Name: {self.name}
    Department: {self.department}
    Type: {self.type}
    Salary: {self.calculate_salary()}
    """

class FullTimeEmployee(Employee):

    def __init__(self, employee_id, name, department,salary):
        super().__init__(employee_id, name, department,type="Full Time")
        self.salary = salary

    def calculate_salary(self):
        return self.salary
    
    def to_dict(self):
        a = {
            "employee_id": self.employee_id,
            "name": self.name,
            "department": self.department,
            "type":self.type,
            "salary":self.salary
        }
        return a
    
class PartTimeEmployee(Employee):
    
    def __init__(self, employee_id, name, department,hour_rate,hours_worked):
        super().__init__(employee_id, name, department,type="Part Time")
        self.hour_rate = hour_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hours_worked*self.hour_rate
    
    def to_dict(self):
        a = {
            "employee_id": self.employee_id,
            "name": self.name,
            "department": self.department,
            "type":self.type,
            "hour_rate": self.hour_rate,
            "hours_worked": self.hours_worked,
            "salary":self.calculate_salary()
        }
        return a