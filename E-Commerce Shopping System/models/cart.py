class Cart:
    
    def __init__(self,customer_id):
        self.customer_id = customer_id
        self.items = []

    def add_item(self,product_id,quantity):
        new = {}
        data = self.find_item(product_id)
        if data!=False:
            data["quantity"] += quantity
        else:
            new["product_id"] = product_id
            new["quantity"] = quantity
            self.items.append(new)

    def remove_item(self,product_id):
        data = self.find_item(product_id)
        if data!=False:
            self.items.remove(data)
            print("Removed Successfully")
        else:
            print("No Product Found")
        
    def find_item(self,product_id):
        for item in self.items:
            if item["product_id"] == product_id:
                return item
        else:
            return False
        
    def update_quantity(self,product_id,quantity):
        data = self.find_item(product_id)
        if data:
            data["quantity"] = quantity
            print("Quantity Updated Successfully")
        else:
            print("Product ID Does Not Exist")

    def clear_cart(self):
        self.items.clear()
        print("Cart Cleared")

    def calculate_total(self, product_service):
        total = 0

        for item in self.items:
            product_id = item["product_id"]
            quantity = item["quantity"]

            product = product_service.check_id(product_id)

            if product != False:
                total += product.price * quantity

        return total

    def to_dict(self):
        a = {
            "customer_id": self.customer_id,
            "items":self.items
        }
        return a
    
    @classmethod
    def from_dict(cls,d):
        cart = cls(d["customer_id"])
        cart.items = d["items"]
        return cart