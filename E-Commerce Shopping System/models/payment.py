from abc import ABC,abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self,customer,amount):
        pass

class WalletPayment(Payment):

    def pay(self,customer,amount):
        if customer.deduct_balance(amount):
            return True, "Payment Successful"
        else:
            return False, "Insufficient Balance"
        
class CardPayment(Payment):

    def pay(self,customer,amount):
        card_number = input("Enter Card Number: ")
        cvv = input("Enter CVV Number: ")
        return True,"Payment Successful"
    
class UPIPayment(Payment):

    def pay(self,customer,amount):
        return True,"Payment Successful"