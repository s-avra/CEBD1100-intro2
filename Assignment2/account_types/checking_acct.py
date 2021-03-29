from babel.numbers import format_currency
from Assignment2.account_types.main_account import Account
class CheckingAccount(Account):
    def withdraw(self,amount):
        if self.balance - amount <0:
            print("Cannot withdraw; Insufficient funds. $15 Overdraft fee charged.")
            self.balance = self.balance-15
        else:
            super().withdraw(amount)
            print(format_currency(amount, 'USD', locale='en_US') + " was successfully withdrawn.")
    def deposit(self, amount):
        super().deposit(amount)
        print(format_currency(amount, 'USD', locale='en_US') + " was successfully deposited.")
    def service_charges(self,amount):
        super().service_charges(amount)
