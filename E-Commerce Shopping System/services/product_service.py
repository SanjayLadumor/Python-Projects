import json
import os
from models.users import User
from models.product import Product

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, '..', 'database', 'products.json')

class ProductService:

    def __init__(self):
        self.products = []

    def add_products(self,product):
        self.products.append(product)
        self.save_products()

    def load_products(self):
        try:
            with open(file_path,"r") as f:
                data = json.load(f)
                for item in data:
                    product = Product.from_dict(item)
                    self.products.append(product)
        except FileNotFoundError:
            print("Database Error Occured")

    def save_products(self):
        data = []
        for item in self.products:
            new = item.to_dict()
            data.append(new)
        with open(file_path,"w") as f:
            json.dump(data,f)

    def check_id(self,a):
        for item in self.products:
            if item.id == a:
                return item
        else:
            return False

    def delete_product(self,id):
        data = self.check_id(id)
        if data!=False:
            self.products.remove(data)
            self.save_products()
            print("Deleted Successfully")
        else:
            print("ID Not Found")
    
    def edit_product(self,id,field,new):
        data = self.check_id(id)
        if data!=False:
            if field=="id":
                check_new = self.check_id(new)
                if check_new==False:
                    data.id = new
                    self.save_products()
                    print("ID Updated Successfully")
                else:
                    print("New ID Already Exists")
            elif field=="name":
                data.name = new
                self.save_products()
                print("Name Updated Successfully")
            elif field=="category":
                data.category = new
                self.save_products()
                print("Name Updated Successfully")
            elif field=="price":
                data.price = int(new)
                self.save_products()
                print("Price Updated Successfully")
            elif field=="quantity":
                data.quantity = int(new)
                self.save_products()
                print("Quantity Updated Successfully")
            else:
                print("Please Select From Available Services")
        else:
            print("ID Already Exists")

    def search_products(self,id):
        data = self.check_id(id)
        if data!=False:
            return data
        else:
            return False
        
    def get_products(self):
        for item in self.products:
            print(item.to_dict())