from product import Product
import json
import os

class Inventory:

    def __init__(self):
        self.inventory = []
        self.current_product = None
        self.file_path = os.path.join(os.path.dirname(__file__), "inventory.json")
        
    def save_data(self):
        data = []
        for items in self.inventory:
            data.append(items.to_dict())
        with open(self.file_path,"w") as f:
            json.dump(data,f)
            print("Saved Successfully")
        
    def load_data(self):
        try:
            with open(self.file_path,"r") as f:
                d = json.load(f)
                for item in d:
                    new = Product(item["id"],item["name"],item["category"],item["price"],item["quantity"])
                    self.inventory.append(new)
        except FileExistsError:
            print("File Does not Exists")

    def check_product(self,a):
        for items in self.inventory:
            if items.id == a:
                return items
        else:
            return False
        
    def validate_id(self,id):
        for items in self.inventory:
            if items.id == id:
                return False
        else:
            return True
        
    def add_product(self):
        id = int(input("Enter Product ID: "))
        if self.validate_id(id):
            name = input("Enter Name: ")
            category = input("Enter Category: ")
            price = int(input("Enter Price: "))
            if price>0:
                quantity = int(input("Enter Quantity: "))
                new = Product(id,name,category,price,quantity)
                self.inventory.append(new)
                self.save_data()
            else:
                print("Price cannot be Negative")
        else:
            print("ID Already Exists")

    def view_products(self):
        for items in self.inventory:
            print(items.to_dict())

    def get_product(self,id):
        for item in self.inventory:
            if item.id == id:
                return item
        else:
            return False

    def search_product(self):
        a = int(input("Enter Product ID: "))
        if not self.validate_id(a):
            for item in self.inventory:
                if item.id == a:
                    print(item.to_dict())
        else:
            print("No ID Found")

    def update_product(self):
        a = int(input("Enter Product ID: "))
        if not self.validate_id(a):
            print("""Select What to Update: 
1. Name
2. Category
3. Price
4. Quantity""")
            try:
                b = int(input("Enter Your Selection: "))
                data = self.get_product(a)
                if b==1:
                    c = input("Enter New Name: ")
                    data.name = c
                    print("Name Updated Successfully")
                elif b==2:
                    c = input("Enter New Category: ")
                    data.category = c
                    print("Category Upadated Successfully")
                elif b==3:
                    c = int(input("Enter New Price: "))
                    if c>0:
                        data.price = c
                        print("Price Updated Successfully")
                    else:
                        print("Price Cannot Be Negative")
                elif b==4:
                    c = int(input("Enter New Quantity: "))
                    data.quantity = c
                    print("Quantity Updated Successfully")
                else:
                    print("Please Select From Given Options")
                self.save_data()
            except ValueError:
                print("Please Enter Integer")

    def delete_product(self):
        a = int(input("Enter Product ID: "))
        if not self.validate_id(a):
            for item in self.inventory:
                if item.id == a:
                    val = item
                    self.inventory.remove(val)
                    self.save_data()
                    print("Removed Successfully")
        else:
            print("No ID Found")

    def low_stock_report(self):
        low_stock = []
        for item in self.inventory:
            if item.quantity <= 3:
                low_stock.append(item.name)
        if len(low_stock)==0:
            print("All Items Are Stocked")
        else:
            print("Items With Low Stock Are:")
            for i in range(len(low_stock)):
                print(f"{i+1}. {low_stock[i]}")

    def inventory_value(self):
        total = 0
        for item in self.inventory:
            print(f"{item.name}")
            print(f"{item.price} x {item.quantity} = {item.price * item.quantity}")
            total += item.price * item.quantity
        print("Inventory Value is:",total)