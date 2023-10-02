class Account:
    def __init__(self, currency, balance):
        self.currency = currency
        self.balance = balance

    def add_amount(self, added_amount):
        my_amount = self.balance + added_amount
        return str(my_amount) + self.currency
    
    def withdrawal(self, withdrawal_amount):
        my_balance = self.balance - withdrawal_amount
        if my_balance > 0:
            return str(my_balance) + self.currency
        else:
            return ("insufficient funds")

class SavingAccount(Account):
    def __init__(self, currency, balance, percentage):
        super().__init__(currency, balance)
        self.percentage = percentage
    
    def percentage_accumulation(self):
        my_percentage = self.balance + self.balance * self.percentage / 100
        return str(my_percentage) + self.currency 


account = Account("AMD", 100)
print (account.add_amount(10))
print (account.withdrawal(50))

saving = SavingAccount("AMD", 100, 10)
print (saving.percentage_accumulation())
