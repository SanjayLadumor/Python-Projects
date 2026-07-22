# 🛒 E-Commerce Shopping System

A console-based **E-Commerce Shopping System built with Python**. This project simulates the basic functionality of an online shopping platform, including customer registration, login, product browsing, cart management, order placement, payment processing, inventory management, and order cancellation.

The project uses **Object-Oriented Programming (OOP)** and **JSON files** for persistent data storage.

---

## 🚀 Features

### 👤 User Management

- Customer registration
- Admin registration
- User login and logout
- User authentication
- Customer and Admin roles

### 📦 Product Management

- Add new products
- View all products
- Search products by ID
- Edit product details
- Delete products
- Manage product stock and quantity

### 🛒 Shopping Cart

- Add products to cart
- View customer cart
- Remove products from cart
- Calculate cart total
- Maintain separate carts for customers

### 💳 Payment System

- Wallet payment
- Payment validation
- Wallet balance deduction
- Insufficient balance handling
- Payment status handling

### 📋 Order Management

- Place orders
- Automatically generate order IDs
- View customer orders
- Cancel orders
- Store product information at the time of purchase
- Track order status

### 📊 Inventory Management

- Check product availability
- Validate requested quantity
- Prevent orders when stock is insufficient
- Automatically reduce stock after successful orders

### 💾 Data Persistence

The application stores data using JSON files, allowing data to remain available after restarting the program.

Data is stored in files such as:

- `users.json`
- `products.json`
- `cart.json`
- `orders.json`

---

## 🏗️ Project Structure

```text
E-Commerce Shopping System/
│
├── main.py
│
├── models/
│   ├── users.py
│   ├── admin.py
│   ├── customer.py
│   ├── product.py
│   ├── cart.py
│   ├── order.py
│   └── payment.py
│
├── services/
│   ├── auth_service.py
│   ├── product_service.py
│   ├── cart_service.py
│   ├── order_service.py
│   └── payment_service.py
│
├── database/
│   ├── users.json
│   ├── products.json
│   ├── cart.json
│   └── orders.json
│
└── README.md
```

---

## 🧠 Concepts Practiced

This project was created to practice and apply Python concepts learned during my learning journey.

### Python Basics

- Variables
- Data Types
- Conditional Statements
- Loops
- Functions
- Lists
- Dictionaries
- Tuples

### Object-Oriented Programming

- Classes and Objects
- Constructors
- Inheritance
- Encapsulation
- Method Overriding
- Class Methods
- Object Relationships

### File Handling

- Reading JSON files
- Writing JSON files
- Persistent data storage
- Handling missing database files
- JSON serialization and deserialization

### Exception Handling

- `try`
- `except`
- Handling invalid user input
- Handling missing files
- Handling invalid operations

### Advanced Python

- Modules
- Packages
- Imports
- `@classmethod`
- `__str__()`
- Service-based architecture

---

## 🔄 Application Flow

```text
Start Application
       │
       ▼
Load Users, Products, Cart and Orders
       │
       ▼
User Registration / Login
       │
       ▼
View Products
       │
       ▼
Add Product to Cart
       │
       ▼
View / Modify Cart
       │
       ▼
Place Order
       │
       ├── Check Customer
       ├── Check Cart
       ├── Check Product Availability
       ├── Check Stock
       ├── Calculate Total
       ├── Process Payment
       ├── Create Order
       ├── Reduce Product Stock
       └── Clear Cart
       │
       ▼
View Orders / Cancel Order
       │
       ▼
Logout / Exit
```
---

## 🛠️ Technologies Used

- **Python**
- **Object-Oriented Programming (OOP)**
- **JSON**
- **File Handling**
- **Exception Handling**

No external Python libraries are required.

---

## ▶️ How to Run

### 1. Clone the Repository

```bash
git clone <your-repository-url>
```

### 2. Navigate to Project Directory

```bash
cd E-Commerce-Shopping-System
```

### 3. Run the Application

```bash
python main.py
```

## 📋 Main Menu

```text
The application provides the following options:

===== E-COMMERCE SYSTEM =====

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
11. Exit
```

## 🎯 Project Goals

```text
The main goal of this project was to build a practical Python application that combines multiple concepts into one complete system.

Through this project, I practiced:

-Designing classes using OOP
-Creating relationships between different classes
-Separating application logic into models and services
-Working with persistent JSON data
-Implementing user authentication
-Managing products and inventory
-Building a shopping cart system
-Processing payments
-Managing customer orders
-Handling errors and invalid input
-Building a multi-service application
```

## 🔮 Future Improvements

```text
Possible improvements for future versions include:

-Add a graphical user interface (GUI)
-Build a web version using Flask or FastAPI
-Replace JSON storage with SQLite or PostgreSQL
-Add password hashing
-Add better input validation
-Add admin-specific menu options
-Add product categories and filtering
-Add product search by name
-Add order timestamps
-Add multiple payment methods
-Add product reviews and ratings
-Add email notifications
-Add automated testing using
```

## 📚 Learning Outcome

This project helped me strengthen my understanding of **Python, Object-Oriented Programming, JSON file handling, exception handling, and basic software architecture** by applying these concepts to a practical E-Commerce application.

It was built as a learning project to improve my Python programming, Object-Oriented Programming, file handling, and problem-solving skills.

## 👨‍💻 Author

### Sanjay Ladumor

BE Computer Science & Engineering (Data Science) Student

⭐ If you found this project useful, feel free to explore the repository and check out my other Python projects.