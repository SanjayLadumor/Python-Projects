class Account:

    def __init__(self,account_number,name,pin,balance=0):
        self.account_number = account_number
        self.name = name
        self.pin = pin
        self.__balance = balance
        self.transactions = []

    def deposit(self,value):
        if value<=0:
            print(f"Amount cannot be Negative")
            return False
        else:
            self.__balance += value
            self.add_transaction(f"Rs.{value} Deposited")
            return True
    
    def withdraw(self,value):
        if value>=self.__balance:
            print(f"Insufficient Balance")
            return False
        elif value<=0:
            print(f"Amount cannot be negative")
            return False
        else:
            self.__balance -= value
            self.add_transaction(f"Rs.{value} Withdrawned")
            return True
        
    def check_balance(self):
        return self.__balance
    
    def add_transaction(self,message):
        self.transactions.append(message)

    def to_dict(self):
        a = {
            "account_number":self.account_number,
            "name":self.name,
            "pin":self.pin,
            "balance":self.__balance,
            "transactions":self.transactions
        }
        return a