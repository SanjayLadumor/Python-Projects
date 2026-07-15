class Product:

    def __init__(self,id,name,category,price,quantity):
        self.id = id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def to_dict(self):
        a = {
            "id":self.id,
            "name":self.name,
            "category":self.category,
            "price":self.price,
            "quantity":self.quantity
        }
        return a
    
    def from_dict(self,dt):
        a = Product(dt["id"],dt["name"],dt["category"],dt["price"],dt["quantity"])
        return a