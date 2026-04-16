import json
import datetime
# BANK MANAGEMENT SYSTEM PROJECT

class BankAccount:

    def __init__(self,account_no, name, balance, pin):
        # Constructor 
        self.account_no=account_no
        self.name = name
        self.balance = balance
        self.pin = pin
        self.history = []  

    # FOR DEPOSITE

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # new timestamp each deposit
            self.history.append(f"[{timestamp}] Deposited {amount}")
            print(f"{amount} deposited successfully at {timestamp}")
        else:
            print("Invalid amount")


    # FOR WITHDRAW (USING SECURITY PIN)


    def withdraw(self, amount, entered_pin):
        if entered_pin == self.pin:
            if amount <= self.balance:
                self.balance -= amount
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # new timestamp each withdrawl
                self.history.append(f"[{timestamp}] withdrawn {amount}")
                print(f"{amount} withdrawn successfully")
            else:
                print("Insufficient balance")
        else:
            print("Incorrect PIN")


    # FOR CHECK BALANCE

    def check_balance(self):
        print(f"💰 Account Balance: {self.balance}")

    
    # SHOW TRANSACTION HISTORY

    def show_history(self):
        print("📜 Transaction History:")
        for h in self.history:
            print(" -", h)


    # FOR TRANSFER MONEY

    def transfer(self, receiver, amount, entered_pin):
        if entered_pin == self.pin:
            if amount <= self.balance:
                self.balance -= amount
                receiver.balance += amount

                # Store history in both accounts

                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # new timestamp each transaction
                self.history.append(f" [{timestamp}] Transferred {amount} to {receiver.name}")
                receiver.history.append(f" [{timestamp}] Received {amount} from {self.name}")

                print("Transfer successful")
            else:
                print("Insufficient balance")
        else:
            print("Incorrect PIN")



# FOR PERMANENTLY STORE MULTIPLE ACCOUNTS 

accounts = []

def save_accounts():                                                    # to save data
    data = []
    for acc in accounts:
        data.append({
            "account_no": acc.account_no,
            "name": acc.name,
            "balance": acc.balance,
            "pin": acc.pin,
            "history": acc.history
        })
    with open("accounts.json", "w") as f:
        json.dump(data, f)


# FUNCTION FOR LOADING DATA 


def load_accounts(): 
    try:
        with open("accounts.json", "r") as f:
            data = json.load(f)
            for acc_data in data:
                acc = BankAccount(
                    acc_data["account_no"],
                    acc_data["name"],
                    acc_data["balance"],
                    acc_data["pin"]
                )
                acc.history = acc_data["history"]
                accounts.append(acc)
    except FileNotFoundError:
        pass



# FUNCTION TO FIND ACCOUNT

def find_account(acc_number):
    for acc in accounts:
        if acc.account_no == acc_number:
            return acc
    return None

# FOR SHOWING ALL ACCOUNTS WHICH IS CREATED

def show_all_accounts():
    print("All Accounts Created:")
    if not accounts:
        print(" - No accounts yet")
    else:
        for acc in accounts:
            print(f"Account No: {acc.account_no}, Name: {acc.name}, Balance: {acc.balance}")


# FOR DELETE ANY ACCOUNT

def delete_account(acc_number):
    acc = find_account(acc_number)  
    if acc:
        accounts.remove(acc)       
        print(f"Account {acc_number} deleted successfully.")
    else:
        print("Account not found")


# MENU-DRIVEN PROGRAM

load_accounts()                                   # LOAD ACCOUNTS WHEN PROGRAM STARTS


while True:
    print("\n===== BANK SYSTEM MENU =====")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Transfer Money")
    print("6. Transaction History")
    print("7. Show All Accounts")
    print("8. Delete Account")
    print("9. Exit")

    choice = int(input("Enter your choice: "))

    
    # IT IS FOR CREATE ACCOUNT
    
    if choice == 1:
        account_no=int(input("enter the account no. : "))
        name = input("Enter name: ")
        balance = float(input("Enter initial balance: "))
        pin = int(input("Set your PIN: "))

        acc = BankAccount(account_no, name, balance, pin)
        accounts.append(acc)

        print(f"Account created successfully!")
        print(f"Your Account Number: {acc.account_no}")

    
    # IT IS FOR DEPOSITE

    elif choice == 2:
        acc_no = int(input("Enter account number: "))
        acc = find_account(acc_no)

        if acc:
            amount = float(input("Enter amount: "))
            acc.deposit(amount)
        else:
            print("Account not found")

    # IT IS FOR WITHDRAW

    elif choice == 3:
        acc_no = int(input("Enter account number: "))
        acc = find_account(acc_no)

        if acc:
            amount = float(input("Enter amount: "))
            pin = int(input("Enter PIN: "))
            acc.withdraw(amount, pin)
        else:
            print("Account not found")

    # IT IS FOR CHECK BANK BALANCE

    elif choice == 4:
        acc_no = int(input("Enter account number: "))
        acc = find_account(acc_no)

        if acc:
            acc.check_balance()
        else:
            print("Account not found")

    # IT IS FOR TRANSFER MONEY

    elif choice == 5:
        sender_no = int(input("Enter your account number: "))
        receiver_no = int(input("Enter receiver account number: "))

        sender = find_account(sender_no)
        receiver = find_account(receiver_no)

        if sender and receiver:
            amount = float(input("Enter amount: "))
            pin = int(input("Enter your PIN: "))
            sender.transfer(receiver, amount, pin)
        else:
            print("Invalid account details")

    # IT IS FOR CHECK TRANSACTION HISTORY

    elif choice == 6:
        acc_no = int(input("Enter account number: "))
        acc = find_account(acc_no)

        if acc:
            acc.show_history()
        else:
            print("Account not found")

    # FOR SHOWING ALL ACCOUNTS

    elif choice == 7:
        show_all_accounts()

    
    # fOR EXIT THE MENU
    
    elif choice == 8:
        acc_no = int(input("Enter account number to delete: "))
        delete_account(acc_no)

    # FOR DELETE ACCOUNT

    elif choice == 9:
        print("Thank you for using Bank System")
        save_accounts()                              # SAVE THE ACCOUNT BEFORE EXIT THE PROGRAM 
        break
    else:
        print("Invalid choice")