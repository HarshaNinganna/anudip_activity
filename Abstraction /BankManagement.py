class Bank:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Amount {amount} has been Deposited to {self.__account_number}")
        else:
            print("Amount must be a positive number")
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Amount {amount} has been Debited from {self.__account_number}")
        else:
            print("Insufficient Balance / Invalid amount")
    
    def get_balance(self):
        return self.__balance
    
    def transfer_amount(self, target_account, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            target_account.__balance += amount  
            print(f"Amount {amount} has been Successfully transferred to {target_account.__account_number}")
        else:
            print("Transfer failed: Invalid Amount / Insufficient Balance")


acc_num1 = int(input("Enter Account Number 1: "))
acc_num2 = int(input("Enter Account Number 2: "))

Account1 = Bank(acc_num1, 0)
Account2 = Bank(acc_num2, 0)

deposit_amount = int(input(f"Enter amount to deposit into Account {acc_num1}: "))
Account1.deposit(deposit_amount)

withdraw_amount = int(input(f"Enter amount to withdraw from Account {acc_num1}: "))
Account1.withdraw(withdraw_amount)
print("Account 1 Balance:", Account1.get_balance())

transfer_amount = int(input(f"Enter amount to transfer from Account {acc_num1} to Account {acc_num2}: "))
Account1.transfer_amount(Account2, transfer_amount)

print("Account 1 Balance after transfer:", Account1.get_balance())
print("Account 2 Balance after receiving:", Account2.get_balance())
