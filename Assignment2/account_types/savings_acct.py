from babel.numbers import format_currency
from Assignment2.account_types.main_account import Account
class SavingsAccount(Account):
    def account_active(self):
        if self.balance < 25:
            return self.account_status == False
        else:
            return self.account_status == True
    def withdraw(self,amount):
        if self.account_status == False:
            print("Account is inactive; minimum balance required is $25.00. ")
        elif (self.balance - amount) < 0:
            print("Cannot withdraw; Insufficient funds.")
        else:
            super().withdraw(amount)
            print(format_currency(amount, 'USD', locale='en_US') + " was successfully withdrawn.")
    def deposit(self, amount):
        super().deposit(amount)
        print(format_currency(amount, 'USD', locale='en_US') + " was successfully deposited.")
    def service_charges(self,amount):
        super().service_charges(amount)



svgacct1=SavingsAccount(30,0.5,True)
print(str(svgacct1.account_status))
svgacct1.withdraw(15)
print(str(svgacct1.account_status))
svgacct1.withdraw(5)
print(str(svgacct1.account_status))
print(str(svgacct1.balance_total()))
print(str(svgacct1.deposit_total))
svgacct1.deposit(60)
svgacct1.deposit(50)
svgacct1.doMonthlyReport()
print(str(svgacct1.starting_balance) + " " + str(svgacct1.deposit_count))
svgacct1.deposit(80)
print(str(svgacct1.balance))
print(str(svgacct1.starting_balance))
