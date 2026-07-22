from datetime import datetime

class Order:

    def __init__(self,order_id,customer_id,items,total_amount,payment_method,status,created_at=None):
        self.order_id = order_id
        self.customer_id = customer_id
        self.items = items
        self.total_amount = total_amount
        self.payment_method = payment_method
        self.status = status
        if created_at is None:
            self.created_at = datetime.now().strftime(
                "%d-%m-%Y %H:%M:%S"
            )
        else:
            self.created_at = created_at

    def __str__(self):
        result = (
            f"\n===== ORDER {self.order_id} =====\n"
            f"Customer ID: {self.customer_id}\n"
            f"Payment Method: {self.payment_method}\n"
            f"Status: {self.status}\n"
            f"Total: {self.total_amount}\n"
            f"Items:\n"
        )

        for item in self.items:
            result += (
                f"  Product: {item['name']} | "
                f"Quantity: {item['quantity']} | "
                f"Price: {item['price_at_purchase']} | "
                f"Subtotal: {item['subtotal']}\n"
            )

        return result

    def to_dict(self):
        return {
            "order_id":self.order_id,
            "customer_id":self.customer_id,
            "items":self.items,
            "total_amount":self.total_amount,
            "payment_method":self.payment_method,
            "status":self.status,
            "created_at":self.created_at
        }

    @classmethod
    def from_dict(cls,d):
        return cls(
            d["order_id"],
            d["customer_id"],
            d["items"],
            d["total_amount"],
            d["payment_method"],
            d["status"],
            d["created_at"]
        )