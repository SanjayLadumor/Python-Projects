from models.users import User

class Customer(User):

    customers = []

    def __init__(self, id, name, email, password, phone,wallet_balance,cart,orders):
        super().__init__(id, name, email, password, phone,"customer")
        self.__wallet_balance = wallet_balance
        self.cart = cart
        self.orders = orders
    
    def add_money(self,amount):
        if amount<=0:
            print("Invalid Amount")
        else:
            self.__wallet_balance += amount

    def show_balance(self):
        return self.__wallet_balance
    
    def deduct_balance(self, amount):
        if amount <= self.__wallet_balance:
            self.__wallet_balance -= amount
            return True
        return False
    
    def to_dict(self):
        data = super().to_dict()
        data["wallet_balance"] = self.show_balance()
        return data
    
    @classmethod
    def from_dict(cls,d):
        return cls(d["id"],d["name"],d["email"],d["password"],d["phone"],d["wallet_balance"],d["cart"],d["orders"])