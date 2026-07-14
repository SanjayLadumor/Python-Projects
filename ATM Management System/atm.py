from account import Account
import json
import os

class ATM:
    
    def __init__(self):
        self.accounts = []
        self.current_user = None
        self.file_path = os.path.join(os.path.dirname(__file__), "accounts.json")

    def load_data(self):
        with open(self.file_path,"r") as f:
            data = json.load(f)
            for acc_data in data:
                account = Account(acc_data["account_number"],acc_data["name"],acc_data["pin"],acc_data["balance"])
                self.accounts.append(account)

    def save_data(self):
        data = []
        for accounts in self.accounts:
            data.append(accounts.to_dict())
        with open(self.file_path,"w") as f:
            json.dump(data,f,indent=3)

    def create_account(self):
        acc_num = int(input("Enter Account Number: "))
        if self.find_account(acc_num):
            print("Account Already Exists")
            return
        else:
            name = input("Enter Name: ")
            pin = int(input("Enter PIN: "))
            new_account = Account(acc_num, name, pin,0)
            self.accounts.append(new_account)
            self.save_data()

            print("Account Created Successfully")

    def find_account(self,account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def login(self):
        account_number = int(input("Enter Account Number: "))
        pin = int(input("Enter PIN: "))
        account = self.find_account(account_number)
        if account and account.pin == pin:
            self.current_user = account
            print(f"Welcome {account.name}")
        else:
            print("Invalid Account Number or PIN")

    def deposit(self):
        if not self.current_user:
            print("Please Login First.")
            return

        amount = float(input("Enter amount to deposit: "))
        print(self.current_user.deposit(amount))
        self.save_data()

    def withdraw(self):
        if not self.current_user:
            print("Please Login First.")
            return
        amount = float(input("Enter amount to Withdraw: "))
        print(self.current_user.withdraw(amount))
        self.save_data()
    
    def check_balance(self):
        if not self.current_user:
            print("Please Login First.")
            return
        print(self.current_user.check_balance())

    def logout(self):
        if self.current_user:
            self.current_user = None
            print("Logged Out Successfully")
        else:
            print("No user is currently logged in.")