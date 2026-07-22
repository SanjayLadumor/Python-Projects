import json
import os
from models.order import Order
from models.cart import Cart
from services.cart_service import CartService
from services.product_service import ProductService
from services.payment_service import PaymentService
from services.auth_service import AuthService

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, '..', 'database', 'orders.json')

class OrderService:

    def __init__(self, auth_service, cart_service, product_service, payment_service):
        self.orders = []

        self.auth_service = auth_service
        self.cart_service = cart_service
        self.product_service = product_service
        self.payment_service = payment_service

    def load_orders(self):
        try:
            with open(file_path,"r") as f:
                data = json.load(f)
                for item in data:
                    order = Order.from_dict(item)
                    self.orders.append(order)
        except FileNotFoundError:
            print("Database Error Occured")

    def save_orders(self):
        data = []
        for item in self.orders:
            new = item.to_dict()
            data.append(new)
        with open(file_path,"w") as f:
            json.dump(data,f)

    def find_order(self,a):
        for item in self.orders:
            if item.order_id == a:
                return item
        else:
            return False

    def cancel_order(self, order_id):
        data = self.find_order(order_id)
        if data == False:
            print("No Order ID Found")
            return
        if data.status == "Cancelled":
            print("Order Already Cancelled")
            return
        
        data.status = "Cancelled"
        self.save_orders()
        print("Order Cancelled Successfully")

    def generate_order_id(self):
        if not self.orders:
            return 1
        max_id = max(order.order_id for order in self.orders)
        return max_id + 1

    def place_order(self, customer_id, payment_method):
        customer = self.auth_service.check_id(customer_id)
        if customer == False:
            print("Customer not found")
            return
        customer_cart = self.cart_service.find_cart(customer_id)

        if customer_cart == False:
            print("Cart not found")
            return

        if not customer_cart.items:
            print("Cart is empty")
            return

        for item in customer_cart.items:
            product_id = item["product_id"]
            quantity = item["quantity"]

            product = self.product_service.check_id(product_id)

            if product == False:
                print("Product Does not Exist")
                return

            if quantity > product.quantity:
                print(f"Insufficient stock for {product.name}")
                return

        total = customer_cart.calculate_total(self.product_service)

        payment_success, message = self.payment_service.process_payment(
            payment_method,
            customer,
            total
        )

        if not payment_success:
            print(message)
            return

        print(message)

        snapshot = []

        for item in customer_cart.items:
            product_id = item["product_id"]
            quantity = item["quantity"]

            product = self.product_service.check_id(product_id)

            subtotal = product.price * quantity

            new = {
                "id": product_id,
                "name": product.name,
                "price_at_purchase": product.price,
                "quantity": quantity,
                "subtotal": subtotal
            }

            snapshot.append(new)

        order_id = self.generate_order_id()

        new_order = Order(
            order_id,
            customer_id,
            snapshot,
            total,
            payment_method,
            "success"
        )

        self.orders.append(new_order)
        self.save_orders()

        for item in customer_cart.items:
            product_id = item["product_id"]
            quantity = item["quantity"]

            product = self.product_service.check_id(product_id)

            product.quantity -= quantity

        self.product_service.save_products()

        customer_cart.clear_cart()

        self.cart_service.save_cart()

        print("Order Placed Successfully")

    def get_orders(self,customer_id):
        all_orders = []
        for item in self.orders:
            if item.customer_id == customer_id:
                all_orders.append(item)
        return all_orders

    def get_order(self,order_id):
        data = self.find_order(order_id)
        if data!=False:
            return data
        else:
            print("No Order ID Found")