from models.payment import WalletPayment
from models.payment import CardPayment
from models.payment import UPIPayment

class PaymentService:

    def process_payment(self,payment_method,customer,amount):

        if payment_method=="wallet":
            payment = WalletPayment()

        elif payment_method=="card":
            payment = CardPayment()

        elif payment_method=="upi":
            payment = UPIPayment()

        else:
            return False,"Invalid Payment Method"
        
        return payment.pay(customer,amount)