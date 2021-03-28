from babel.numbers import format_currency


class Account:

    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.starting_balance = 0 + balance
        self.withdraw_count = 0
        ##deposit count starting at zero to keep monthly deposit count accurate. Starting balance not included in deposit total.
        self.deposit_count = 0
        self.deposit_total = 0
        self.withdraw_total = 0
        self.interest_rate = interest_rate
        self.service_charge = 0
        self.account_status = ""

    def calculate_interest(self):
        return (self.interest_rate/12)*self.balance

    def withdraw(self, amount):
        self.balance = self.balance - amount
        self.withdraw_count += 1
        self.withdraw_total += amount

    def deposit(self, amount):
        self.balance = self.balance + amount
        self.deposit_count += 1
        self.deposit_total += amount

    def balance_total(self):
        return self.calculate_interest()+self.balance

    def service_charges(self, amount):
        self.service_charge += amount
        self.balance =self.balance - amount
    def account_active(self):
        if self.balance < 25:
           return self.account_status == "Inactive"
        else:
           return self.account_status == "Active"

    def doMonthlyReport(self):
        print("Account Status: " + str(self.account_active()))
        print("Starting Balance: " + format_currency(self.starting_balance,'USD',locale= 'en_US'))
        print("Total Deposits: " + format_currency(self.deposit_total,'USD', locale= 'en_US'))
        print("Total Number of Deposits: " + str(self.deposit_count))
        print("Total Withdrawals: " + format_currency(self.withdraw_total,'USD', locale= 'en_US'))
        print("Total Number of Withdrawals: " + str(self.withdraw_count))
        print("Service Charges: " + format_currency(self.service_charge,'USD', locale= 'en_US'))
        print("Interest Generated: " + format_currency(self.calculate_interest(),'USD',locale='en_US'))
        print("Current Balance: " + format_currency(self.balance_total(),'USD',locale='en_US'))
        self.balance = self.balance_total()
        self.starting_balance = 0 + self.balance
        self.deposit_total = 0
        self.withdraw_total = 0
        self.deposit_count = 0
        self.withdraw_count = 0
