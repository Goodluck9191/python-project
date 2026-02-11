

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f'you deposited {amount}. Your new balance is {self.balance}')

    def withdrwal (self, amount):
        if amount > self.balance:
            print('insufficient funds')
        else:
            self.balance -= amount
            print(f'you withdrew {amount}. Your new balance is {self.balance}')

account1 = BankAccount("goodluck", 1000)
account1.deposit(500)
account12 = BankAccount("emeka", 2000)
account12.withdrwal(2500)