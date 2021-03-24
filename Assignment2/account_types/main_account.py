class Account:

    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.starting_balance = 0 + balance
        self.withdraw_count = 0
        self.deposit_count = 0
        self.deposit_total = 0
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

    def service_charges(self,amount):
        return self.service_charge + amount

    def doMonthlyReport(self):
        if self.account_active == True:
           print("Account Status: Active")
        else:
           print("Account Status: Inactive")
        print("Starting Balance: " + str(self.starting_balance))
        print("Total Deposits: " + str(self.deposit_total))
        print("Total Number of Deposits: " + str(self.deposit_count))
        print("Total Withdrawals: " + str(self.withdraw_total))
        print("Total Number of Withdrawals: " + str(self.withdraw_count))
        print("Service Charges: " + str(self.service_charge))
        print("Interest Generated: " + str(self.calculate_interest()))
        print("Current Balance: " + str(self.balance_total()))
