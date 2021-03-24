from babel.numbers import format_currency
from Assignment2.account_types.main_account import Account
class SavingsAccount(Account):
    def withdraw(self,amount):
        if self.balance < 25:
            self.account_active == False
            print("Account is inactive; minimum balance required is $25.00. ")
        elif (self.balance - amount) < 0:
            print("Insufficent funds.")
        else:
            super().withdraw(amount)
            print(format_currency(amount, 'USD', locale='en_US') + " was successfully withdrawn.")
    def deposit(self, amount):
        if self.balance + amount <=25:
            super().deposit(amount)
            self.account_active == True
        else:
            super().deposit(amount)
            self.account_active == False
        print(format_currency(amount, 'USD', locale='en_US') + " was successfully deposited.")

svgacct1=SavingsAccount(30,0.5)
print(str(svgacct1.balance_total())+" "+str(svgacct1.starting_balance))
print(str(svgacct1.account_active))
svgacct1.withdraw(15)
print(str(svgacct1.account_active))
svgacct1.withdraw(15)
print(str(svgacct1.account_active))
print(str(svgacct1.balance_total()))
print(str(svgacct1.deposit_total))
svgacct1.deposit(60)
svgacct1.deposit(50)
svgacct1.doMonthlyReport()