from babel.numbers import format_currency
from Assignment2.account_types.main_account import Account
class SavingsAccount(Account):
    def withdraw(self,amount):
        if self.account_status == False:
            print("Account is inactive; minimum balance required is $25.00. ")
        elif (self.balance - amount) < 0:
            print("Cannot withdraw; Insufficent funds.")
        else:
            super().withdraw(amount)
            super().account_active()
            print(format_currency(amount, 'USD', locale='en_US') + " was successfully withdrawn.")
    def deposit(self, amount):
        if self.balance + amount <=25:
            super().deposit(amount)
            self.account_status == True
        else:
            super().deposit(amount)
            self.account_status == False
        print(format_currency(amount, 'USD', locale='en_US') + " was successfully deposited.")
    def service_charges(self,amount):
        super().service_charges(amount)

    def doMonthlyReport(self):
        if self.account_status == True:
           print("Account Status: Active")
        else:
           print("Account Status: Inactive")
        super().doMonthlyReport()



svgacct1=SavingsAccount(30,0.5)
print(str(svgacct1.account_status))
svgacct1.withdraw(15)
print(str(svgacct1.account_status))
svgacct1.withdraw(15)
print(str(svgacct1.account_status))
print(str(svgacct1.balance_total()))
print(str(svgacct1.deposit_total))
svgacct1.deposit(60)
svgacct1.deposit(50)
svgacct1.doMonthlyReport()