class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Додано {amount} до балансу. Поточний баланс: {self.balance}")
        else:
            print("Сума для поповнення повинна бути більше нуля.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостатньо коштів на рахунку для здійснення операції.")
        elif amount <= 0:
            print("Сума для зняття повинна бути більше нуля.")
        else:
            self.balance -= amount
            print(f"Знято {amount}. Поточний баланс: {self.balance}")

account = BankAccount("123456789", 500)
account.deposit(500)
account.withdraw(1001)
account.deposit(0)
account.withdraw(678)