import os
import json

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, '..', 'database', 'products.json')

class Product:

    def __init__(self,id,name,category,price,quantity):
        self.id = id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def to_dict(self):
        a = {
            "id" : self.id,
            "name" : self.name,
            "category" : self.category,
            "price" : self.price,
            "quantity" : self.quantity,
        }
        return a
    
    @classmethod
    def from_dict(cls, d):
        return cls(
            d["id"],
            d["name"],
            d["category"],
            d["price"],
            d["quantity"]
        )