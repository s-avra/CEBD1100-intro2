class Account:

    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.starting_balance = 0 + balance
        self.withdraw_count = 0
        self.deposit_count = 0
        self.deposit_total = 0+balance
        self.withdraw_total= 0
        self.interest_rate = interest_rate
        self.service_charge = 0
        self.account_active = True
    def calculate_interest(self):
        return (self.interest_rate/12)*self.balance

    def withdraw(self, amount):
        if amount < 0:
            print("Cannot withdraw negative amount.")
        else:
            self.balance = self.balance - amount
            self.withdraw_count += 1
            self.withdraw_total += amount

    def deposit(self, amount):
        if amount <0:
            print("Cannot deposit negative amount.")
        else:
            self.balance = self.balance + amount
            self.deposit_count += 1
            self.deposit_total += amount

    def balance_total(self):
        return self.calculate_interest()+self.balance

    def doMonthlyReport(self):
        return
        print("report")