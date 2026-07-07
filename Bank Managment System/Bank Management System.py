def show_menu():
    print(""""
======== BANK MENU ========

1. Create Account
2. Deposit
3. Withdraw
4. Transfer
5. Check Balance
6. Transaction History
7. Delete Account
8. Exit
          """)
    
accounts = [
    {
    "name":"Sadie Sink",
    "id":12,
    "adhhar":12345,
    "address":"New York",
    "balance":30000,
    "history":[]
    },
    {
    "name":"Karen Page",
    "id":10,
    "adhhar":1245,
    "address":"New York",
    "balance":20000,
    "history":[]
    },
]

def find_account(a):
    for i in range(len(accounts)):
        if accounts[i]["id"]==a:
            return f"Account Found"
    else:
        return f"Account Not Found"
    
def create_account():
    new_acc = {}
    new_acc["name"] = input("Enter Name: ")
    new_acc["id"] = int(input("Enter Your ID: "))
    new_acc["adhhar"] = int(input("Enter Adhhaar Number: "))
    new_acc["address"] = input("Enter Address: ")
    new_acc["balance"] = 0
    new_acc["history"] = []
    accounts.append(new_acc)
    return accounts

def deposit():
    b = int(input("Enter Bank ID: "))
    for i in range(len(accounts)):
        if accounts[i]["id"]==b:
            print("Account Found")
            a = int(input("Enter Amount to Deposit: "))
            accounts[i]["balance"] += a
            data = f"Rs.{a} Deposited"
            accounts[i]["history"].append(data)
            print(f"Deposited Rs.{a} Successfully")
            break
    else:
        return f"No Account Found"
    
def withdraw():
    a = int(input("Enter Bank ID: "))
    for i in range(len(accounts)):
        if accounts[i]["id"]==a:
            print("Account Found")
            acc_balance = accounts[i]["balance"]
            b = int(input("Enter Amount to Withdraw: "))
            if b>acc_balance :
                print("Insufficient Balance")
            else:
                new_bal = acc_balance - b
                accounts[i]["balance"] = new_bal
                data = f"Rs.{b} Withdrawned"
                accounts[i]["history"].append(data)
                return f"Withdrawned Rs.{b} Successfully"
            break
    else:
        return f"No Account Found"

def transfer():

    a = int(input("Enter Bank ID to Transfer From: "))
    for i in range(len(accounts)):
        if accounts[i]["id"]==a:
            print("Account Found!")
            break
    else:
        print(f"No Account Found")
        print("Please Check ID Again")
        transfer()

    b = int(input("Enter Bank ID to Transfer To: "))
    for u in range(len(accounts)):
        if accounts[u]["id"]==b:
            print("Account Found!")
            break
    else:
        print(f"No Account Found")
        print("Please Check ID Again")
        transfer()

    c = int(input("Enter Amount to Transfer: "))
    for m in range(len(accounts)):
        if accounts[m]["id"]==a:
            if accounts[m]["balance"]>c:
                accounts[m]["balance"] -= c
                data = f"Rs.{c} Transferred"
                accounts[m]["history"].append(data)
                return f"Rs.{c} Tranfferred Successfully"
            else:
                print("Insufficient Balance")
    for j in range(len(accounts)):
        if accounts[j]["id"]==b:
            accounts[j]["balance"] += c
            data = f"Rs.{c} Received"
            accounts[j]["history"].append(data)
            return f"Rs.{c} Tranfferred Successfully"
    
def check_balance():
    a = int(input("Enter Bank ID: "))
    for i in range(len(accounts)):
        if accounts[i]["id"]==a:
            print("Account Found!!")
            bal = accounts[i]["balance"]
            return f"Balance is: {bal}"
    else:
        print("No Account Found")

def transaction_history():  
    a = int(input("Enter Bank ID: "))
    for i in range(len(accounts)):
        if accounts[i]["id"]==a:
            print(accounts[i]["history"])
            break
    else:
        print("Account Not Found")

def delete_account():
    a = int(input("Enter Bank ID: "))
    for i in range(len(accounts)):
        if accounts[i]["id"]==a:
            del accounts[i]
            print(f"Account Deleted Successfully")
            break
    else:
        return f"Account Not Found"

def main():
    Bank_Open = True

    while Bank_Open:
        show_menu()
        a = int(input("Your Selection: "))
        if a==1:
            print(create_account())
        elif a==2:
            print(deposit())
        elif a==3:
            print(withdraw())
        elif a==4:
            print(transfer())
        elif a==5:
            print(check_balance())
        elif a==6:
            print(transaction_history())
        elif a==7:
            print(delete_account())
        elif a==8:
            Bank_Open = False
        else:
            print("Please Enter a Valid Choice")
            
main()