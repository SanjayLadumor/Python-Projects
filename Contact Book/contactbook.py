from contacts import Contact
import os
import json
import re

class ContactBook:

    def __init__(self):
        self.contacts = []
        self.file_path = os.path.join(os.path.dirname(__file__), "contacts.json")

    def save_contacts(self):
        data = []
        for contact in self.contacts:
            data.append(contact.to_dict())

        with open(self.file_path,"w") as f:
            json.dump(data,f)
        
        print("Data Saved Successfully")

    def load_contacts(self):
        self.contacts.clear()
        with open(self.file_path,"r") as f:
            data = json.load(f)
            for ele in data:
                new = Contact(ele["name"],ele["phone"],ele["email"],ele["address"])
                self.contacts.append(new)
            print("Loaded Successfully")

    def validate_phone(self,a):
        pattern = "^\\d{10}$"
        if re.findall(pattern,a):
            return True
        else:
            return False
    
    def validate_email(self,a):
        pattern = "^[A-Za-z0-9]+@[a-z]+\\.[a-z]+$"
        if re.findall(pattern,a):
            return True
        else:
            return False
        
    def duplicate_phone(self,phone):
        for contact in self.contacts:
            if contact.phone == phone:
                return False
        else:
            return True
        
    def duplicate_email(self,email):
        for contact in self.contacts:
            if contact.email == email:
                return False
        else:
            return True

    def display_contact(self):
        a = input("Enter Name: ")
        data = self.find_contact(a)
        if data==None:
            print("No Contact Found")
        else:
            print(data.display())

    def find_contact(self,a):
        for contact in self.contacts:
            if contact.name.lower() == a.lower():
                return contact
        else:
            return None
        
    def add_contact(self):
        name = input("Enter Name: ")
        phone = input("Enter Phone: ")
        a = self.validate_phone(phone)
        if a:
            d = self.duplicate_phone(phone)
            if d:
                email = input("Enter Email: ")
                x = self.validate_email(email)
                if x:
                    m = self.duplicate_email(email)
                    if m:
                        address = input("Enter Address: ")
                        new = Contact(name,phone,email,address)
                        self.contacts.append(new)
                        self.save_contacts()
                    else:
                        print("Email Already Exists")
                else:
                    print("Invalid Email")
            else:
                print("Phone Already Exits")
        else:
            print("Invalid Phone")

    def view_contacts(self):
        for contact in self.contacts:
            print(contact.display())
        if not self.contacts:
            print("No contacts found")
            return

    def search_contact(self):
        a = input("Enter Name: ")
        data = self.find_contact(a)
        if data==None:
            print("No Contact Found")
        else:
            print(data.to_dict())

    def update_contact(self):
        a = input("Enter Name: ")
        data = self.find_contact(a)
        if data==None:
            print("No Contact Found")
        else:
            print("""Select To Update: 
1. Phone
2. Email
3. Address""")
            try:
                b = int(input("Enter Your Choice: "))
                if b==1:
                    x = input("Enter New Phone: ")
                    m = self.validate_phone(x)
                    if m:
                        d = self.duplicate_phone(x)
                        if d:
                            data.phone = x
                        else:
                            print("Phone Already Exists")
                    else:
                        print("Invalid Phone")
                elif b==2:
                    x = input("Enter New Email: ")
                    l = self.validate_email(x)
                    if l:
                        m = self.duplicate_email(x)
                        if m:
                            data.email = x
                        else:
                            print("Email Already Exists")
                    else:
                        print("Invalid Email")
                elif b==3:
                    x = input("Enter New Address: ")
                    data.address = x
                else:
                    print("Enter From Given Choices")
                self.save_contacts()
            except ValueError:
                print("Enter Integer")
                return
            
    def delete_contact(self):
        a = input("Enter Name: ")
        data = self.find_contact(a)
        if data==None:
            print("No Contact Found")
        else:
            self.contacts.remove(data)
            self.save_contacts()
            print("Delelted Successfully")