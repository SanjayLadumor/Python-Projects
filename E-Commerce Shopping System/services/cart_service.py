from models.cart import Cart
import json
import os


current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, '..', 'database', 'carts.json')


class CartService:

    def __init__(self):
        self.carts = []

    def save_cart(self):
        data = []

        for cart in self.carts:
            data.append(cart.to_dict())

        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)

    def load_cart(self):
        try:
            with open(file_path, "r") as f:
                data = json.load(f)

                self.carts = []

                for item in data:
                    cart = Cart.from_dict(item)
                    self.carts.append(cart)

        except FileNotFoundError:
            print("Database Error Occured")

        except json.JSONDecodeError:
            print("Cart database is empty or corrupted")
            self.carts = []

    def find_cart(self, customer_id):
        for cart in self.carts:
            if cart.customer_id == customer_id:
                return cart

        return False

    def add_item(self, customer_id, product_id, quantity):
        cart = self.find_cart(customer_id)

        if cart == False:
            cart = Cart(customer_id)
            self.carts.append(cart)

        cart.add_item(product_id, quantity)

        self.save_cart()

        print("Product Added To Cart Successfully")

    def get_cart(self, customer_id):
        cart = self.find_cart(customer_id)

        if cart == False:
            print("Cart Not Found")
            return

        if not cart.items:
            print("Cart Is Empty")
            return

        print("===== YOUR CART =====")

        for item in cart.items:
            print(
                f"Product ID: {item['product_id']} | "
                f"Quantity: {item['quantity']}"
            )

    def remove_item(self, customer_id, product_id):
        cart = self.find_cart(customer_id)

        if cart == False:
            print("Cart Not Found")
            return

        item = cart.find_item(product_id)

        if item == False:
            print("Product Not Found In Cart")
            return

        cart.remove_item(product_id)

        self.save_cart()

        print("Product Removed From Cart Successfully")

    def update_quantity(self, customer_id, product_id, quantity):
        cart = self.find_cart(customer_id)

        if cart == False:
            print("Cart Not Found")
            return

        cart.update_quantity(product_id, quantity)

        self.save_cart()

    def clear_cart(self, customer_id):
        cart = self.find_cart(customer_id)

        if cart == False:
            print("Cart Not Found")
            return

        cart.clear_cart()

        self.save_cart()

        print("Cart Cleared Successfully")

    def checkout(self, customer_id):
        cart = self.find_cart(customer_id)

        if cart == False:
            print("Cart Not Found")
            return

        if not cart.items:
            print("Cart Is Empty")
            return

        cart.clear_cart()

        self.save_cart()

        print("Checkout Successful")