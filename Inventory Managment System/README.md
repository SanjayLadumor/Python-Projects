# 📦 Inventory Management System

A command-line Inventory Management System built with Python that allows users to manage products, track stock levels, and store inventory data using JSON file handling.

## ✨ Features

- ➕ Add new products
- 📋 View all products
- 🔍 Search products by ID
- ✏️ Update product details
- ❌ Delete products
- ⚠️ Low stock report
- 💾 Automatic data saving using JSON
- 📂 Automatic data loading on startup
- ✅ Unique Product ID validation
- ✅ Input validation for product price

---

## 🛠️ Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- JSON
- File Handling
- Exception Handling

---

## 📁 Project Structure

```
Inventory Management System/
│
├── main.py
├── inventory.py
├── product.py
├── inventory.json
└── README.md
```

---

## 🚀 How to Run

1. Clone the repository

```bash
git clone <repository-url>
```

2. Navigate to the project folder

```bash
cd "Inventory Management System"
```

3. Run the program

```bash
python main.py
```

---

## 📋 Menu

```
========== Inventory Management ==========
1. Add Product
2. View Products
3. Search Product
4. Update Product
5. Delete Product
6. Low Stock Report
7. Save & Exit
```

---

## 📦 Product Information

Each product contains:

- Product ID
- Name
- Category
- Price
- Quantity

Example:

```json
{
    "id": 101,
    "name": "Keyboard",
    "category": "Electronics",
    "price": 999,
    "quantity": 15
}
```

---

## 📚 Concepts Practiced

- Classes and Objects
- Object-Oriented Programming
- Constructors
- Methods
- JSON Serialization
- File Handling
- Exception Handling
- Input Validation
- Lists and Dictionaries

---

## 🎯 Future Improvements

- Search by product name
- Sort products by price
- Sort products alphabetically
- Inventory value calculation
- Export inventory to CSV
- Import products from CSV
- Database support using SQLite
- GUI using Tkinter or PyQt
- Barcode support

---

## 👨‍💻 Author

**Sanjay Ladumor**

First-year B.E. Computer Science (Data Science)

Learning Python by building real-world projects 🚀