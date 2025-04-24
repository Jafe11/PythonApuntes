class BankAccount:
    def __init__(self, accountHolder, balance):
        self.account_holder = accountHolder
        self.balance = balance
        self.is_active = True
    
    def deposit(self, amount):
        if self.is_active:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else: 
            print("Account is not active. Cannot deposit.")

    def withdraw(self, amount):
        if self.is_active:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance is {self.balance}.")
            else:
                print("Insufficient funds.")
        else:
            print("Account is not active. Cannot withdraw.")
        
    def desactivateAccount (self):
        self.is_active = False
        print("Account has been deactivated.")

    def activateAccount (self):
        self.is_active = True
        print("Account has been activated.")

account1 = BankAccount("Juan", 1000)
account1.deposit(500)
account1.withdraw(200)
account1.desactivateAccount()
account1.withdraw(300)
account1.activateAccount()