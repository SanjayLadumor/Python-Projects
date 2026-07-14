from atm import ATM

def bank_atm():

    atm = ATM()
    atm.load_data()
    
    atm_open = True
    while atm_open:
        print("""===== ATM =====

    1. Create Account
    2. Login
    3. Deposit
    4. Withdraw
    5. Check Balance
    6. Logout
    7. Exit""")
        a = int(input("Enter Your Choice: "))
        if a==1:
            atm.create_account()
        elif a==2:
            atm.login()
        elif a==3:
            atm.deposit()
        elif a==4:
            atm.withdraw()
        elif a==5:
            atm.check_balance()
        elif a==6:
            atm.logout()
        elif a==7:
            atm_open = False
        else:
            print("Please Choose from Given Options")

bank_atm()