import datetime
OFFICE_START = 9
OFFICE_END = 17
MAX_DEPOSIT_AMOUNT = 50000
customerslist = [
    {'uname': 'Sowmya', 'upwd': 'sowmya', 'secq': 'what is your pet name: ', 'seca': "chotu", 'balance': 100000},
    {'uname': 'Sowmith', 'upwd': 'sowmith', 'secq': 'what is your school name: ', 'seca': "srkr", 'balance': 50000}
]

def is_office_hours():
    now = datetime.datetime.now()
    return now.weekday() < 5 and OFFICE_START <= now.hour < OFFICE_END

def UserSignUp():
    user = {}
    user['uname'] = input("Enter Customer Name: \n")
    user['upwd'] = input("Enter Password: \n")
    user['secq'] = input("Enter security question: \n")
    user['seca'] = input("Enter security answer: \n")
    user['balance'] = 0
    customerslist.append(user)
    print("SignUp Successful!")

def showBalance(user):
    print(f"Current Balance: ₹{user['balance']}")

def deposit(user):
    if not is_office_hours():
        print("Deposits are allowed only during office hours on working days.")
        return
    
    amount = int(input("Enter deposit amount: "))
    if amount > MAX_DEPOSIT_AMOUNT:
        print(f"Deposit amount exceeds the maximum limit of ₹{MAX_DEPOSIT_AMOUNT}.")
        return

    user['balance'] += amount
    print(f"Deposit successful! New Balance: ₹{user['balance']}")

def withdraw(user):
    if not is_office_hours():
        print("Withdrawals are allowed only during office hours on working days.")
        return
    
    amount = int(input("Enter withdrawal amount: "))
    if amount > user['balance']:
        print("Insufficient funds.")
        return

    user['balance'] -= amount
    print(f"Withdrawal successful! New Balance: Rs{user['balance']}")

def fundTransfer(user):
    recipient_name = input("Enter recipient name: ")
    recipient = next((u for u in customerslist if u['uname'] == recipient_name), None)

    if not recipient:
        print("Recipient not found.")
        return

    amount = int(input("Enter transfer amount: "))
    if amount > user['balance']:
        print("Insufficient funds for transfer.")
        return

    user['balance'] -= amount
    recipient['balance'] += amount
    print(f"Fund transfer successful! New Balance: ₹{user['balance']}")

def customerMenu(user):
    while True:
        print("\nCustomer Menu")
        print("1) Show Balance\n2) Deposit\n3) Withdraw\n4) Fund Transfer\n5) Exit\n")
        choice = int(input("Enter choice: "))
        
        if choice == 1:
            showBalance(user)
        elif choice == 2:
            deposit(user)
        elif choice == 3:
            withdraw(user)
        elif choice == 4:
            fundTransfer(user)
        elif choice == 5:
            print("Exiting to main menu.\n")
            break
        else:
            print("Invalid choice. Please try again.")

def UserSignIn():
    name = input("Enter Username: ")
    pwd = input("Enter Password: ")
    x = 1
    y = 1
    for user in customerslist:
        if user['uname'] == name and user['upwd'] == pwd:
            print(f"Welcome, {user['uname']}!")
            customerMenu(user)
            x = 0
            y = 0
            break
        if user['uname'] == name and user['upwd'] != pwd:
            x = 0
        if user['uname'] != name and user['upwd'] == pwd:
            y = 0
    if x == 1 and y == 1:
        print("Invalid User name and password")
    elif x == 0 and y == 1:
        print("Invalid password")
    elif x == 1 and y == 0:
        print("Invalid username")

while True:
    print("\nMain Menu")
    print("1) Customer SignUp\n2) Customer SignIn\n3) Exit\n")
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        UserSignUp()
    elif choice == 2:
        UserSignIn()
    elif choice == 3:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
