# 🏧 ATM Management System (Python OOP)

A console-based ATM Management System built using **Python**, **Object-Oriented Programming (OOP)**, and **JSON** for persistent data storage.

This project simulates the basic functionalities of an ATM such as account creation, login, deposits, withdrawals, balance inquiry, and logout while storing account data permanently in a JSON file.

---

## 🚀 Features

- Create a new bank account
- Secure login using Account Number and PIN
- Deposit money
- Withdraw money
- Check account balance
- Logout
- Prevent duplicate account creation
- Persistent data storage using JSON
- Transaction recording

---

## 🛠️ Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- JSON
- File Handling

---

## 📂 Project Structure

```
ATM Management System/
│
├── account.py        # Account class
├── atm.py            # ATM class
├── main.py           # Program entry point
├── accounts.json     # Stores account data
└── README.md
```

---

## 📚 OOP Concepts Used

- Classes & Objects
- Encapsulation
- Constructors
- Object Interaction
- Method Calling
- Modular Programming

---

## 💾 Data Storage

All account information is stored inside `accounts.json`.

Example:

```json
[
    {
        "account_number": 101,
        "name": "John",
        "pin": 1234,
        "balance": 5000,
        "transactions": [
            "Rs.500 Deposited",
            "Rs.200 Withdrawn"
        ]
    }
]
```

This allows account information to persist even after closing the program.

---

## ▶️ How to Run

1. Clone the repository

```bash
git clone <repository-url>
```

2. Navigate to the project folder

```bash
cd "ATM Management System"
```

3. Run the program

```bash
python main.py
```

---

## 📸 Menu

```
===== ATM =====

1. Create Account
2. Login
3. Deposit
4. Withdraw
5. Check Balance
6. Logout
7. Exit
```

---

## 🎯 Learning Outcomes

Through this project, I practiced:

- Object-Oriented Programming
- Working with multiple Python modules
- JSON serialization and deserialization
- File handling
- Data persistence
- User authentication
- Writing modular and reusable code

---

## 🚀 Future Improvements

- Transfer money between accounts
- Change PIN
- View transaction history
- Delete account
- Input validation using exception handling
- Savings and Current Account using inheritance
- Better terminal UI

---

## 👨‍💻 Author

**Sanjay Ladumor**

If you found this project helpful, feel free to ⭐ the repository.