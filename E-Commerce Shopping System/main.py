from models.users import User
from models.admin import Admin
from models.cart import Cart
from models.customer import Customer
from models.order import Order
from models.payment import Payment
from models.product import Product
from services.auth_service import AuthService
from services.cart_service import CartService
from services.order_service import OrderService
from services.payment_service import PaymentService
from services.product_service import ProductService

def main():
    online = True
    auth = AuthService()
    product = ProductService()
    cart = CartService()
    payment = PaymentService()
    order = OrderService(
                auth,
                cart,
                product,
                payment
            )

    auth.load_users()
    product.load_products()
    cart.load_cart()
    order.load_orders()

    while online:
        print("""===== E-COMMERCE SYSTEM =====

1. Register
2. Login
3. View Products
4. Add Product to Cart
5. View Cart
6. Remove Product from Cart
7. Place Order
8. View My Orders
9. Cancel Order
10. Logout
11. Exit""")
        try:
            a = int(input("Enter Your Choice: "))
            if a==1:
                b = input("Register Customer or Admin: ")
                if b.lower()=="admin":
                    id = int(input("Enter ID: "))
                    name = input("Enter Name: ")
                    email = input("Enter Email: ")
                    password = input("Enter Password: ")
                    phone = int(input("Enter Phone: "))
                    auth.register_admin(id,name,email,password,phone)
                elif b.lower()=="customer":
                    id = int(input("Enter ID: "))
                    name = input("Enter Name: ")
                    email = input("Enter Email: ")
                    password = input("Enter Password: ")
                    phone = int(input("Enter Phone: "))
                    wallet_balance = int(input("Enter Wallet Balance: "))
                    customer_id = int(input("Enter Customer ID: "))
                    customer_cart = Cart(customer_id)
                    orders = []
                    auth.register_customer(id,name,email,password,phone,wallet_balance,customer_cart,orders)
            elif a==2:
                id = int(input("Enter ID: "))
                passwrd = input("Enter Password: ")
                auth.login(id,passwrd)
                user_data = auth.current_user
            elif a==3:
                if auth.current_user is None:
                    print("Please login first")
                else:
                    product.get_products()
            elif a==4:
                if auth.current_user is None:
                    print("Please login first")
                else:
                    user_data = auth.current_user
                    product_id = int(input("Enter Product ID: "))
                    quan = int(input("Enter Quantity: "))
                    cart.add_item(user_data.id, product_id, quan)
            elif a==5:
                if auth.current_user is None:
                    print("Please login first")
                else:
                    user_data = auth.current_user
                    cart.get_cart(user_data.id)
            elif a==6:
                if auth.current_user is None:
                    print("Please login first")
                else:
                    user_data = auth.current_user
                    product_id = int(input("Enter Product ID: "))
                    cart.remove_item(user_data.id, product_id)
            elif a==7:
                if auth.current_user is None:
                    print("Please login first")
                else:
                    user_data = auth.current_user
                    payment_method = input("Enter Payment Method: ")
                    order.place_order(user_data.id,payment_method)
            elif a == 8:
                if auth.current_user is None:
                    print("Please login first")
                else:
                    user_data = auth.current_user
                    orders = order.get_orders(user_data.id) 
                    for item in orders:
                        print(item)
            elif a==9:
                if auth.current_user is None:
                    print("Please login first")
                else:
                    order_id = int(input("Enter Order ID: "))
                    order.cancel_order(order_id)
            elif a==10:
                auth.logout()
            elif a==11:
                online = False
            else:
                print("Invalid Input")
        except ValueError:
            print("Please Enter integer")

if __name__ == "__main__":
    main()