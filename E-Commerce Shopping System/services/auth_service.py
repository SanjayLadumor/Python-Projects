import json
import os
from models.customer import Customer
from models.admin import Admin

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, '..', 'database', 'users.json')

class AuthService:

    def __init__(self):
        self.users = []
        self.current_user = None

    def load_users(self):
        try:
            with open(file_path,"r") as f:
                data = json.load(f)
                for user in data:
                    if user["role"]=="admin":
                        new_user = Admin.from_dict(user)
                    elif user["role"] == "customer":
                        new_user = Customer.from_dict(user)
                    else:
                        continue
                    self.users.append(new_user)
        except FileNotFoundError:
            print("Database Error Occured")

    def save_users(self):
        data = []
        for user in self.users:
            data.append(user.to_dict())
        try:
            with open(file_path,"w") as f:
                json.dump(data,f)
        except FileNotFoundError:
            print("Database Error Occured")

    def check_id(self,id):
        for item in self.users:
            if item.id == id:
                return item
        else:
            return False

    def register_customer(self,id,name,email,password,phone,wallet_balance,cart,orders):
        data = self.check_id(id)
        if data==False:
            new_user = Customer(id,name,email,password,phone,wallet_balance,cart,orders)
            self.users.append(new_user)
            self.save_users()
            print("Registered Customer Successfully")
        else:
            print("ID Already Exists")

    def register_admin(self,id,name,email,password,phone):
        data = self.check_id(id)
        if data==False:
            new_user = Admin(id,name,email,password,phone)
            self.users.append(new_user)
            self.save_users()
            print("Registered Admin Successfully")
        else:
            print("ID Already Exists")

    def login(self,id,password):
        try:
            data = self.check_id(id)
            if data!=False:
                if data.password == password:
                    print("Logged in Successfully")
                    self.current_user = data
                else:
                    print("Invalid Password")
            else:
                print("Invalid ID")
        except ValueError:
            print("Please Enter Integer")

    def logout(self):
        if self.current_user!=None:
            self.current_user = None
            print("Logged Out")
        else:
            print("Not Logged In")