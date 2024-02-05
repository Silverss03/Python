class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name) :
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name
    def deposit(self, money):
        self.balance += money 
        return self.balance
    def withdraw(self, money):
        if(money >= self.balance):
            self.balance -= money
            return self.balance
    def check_balance(self):
        return self.balance
    def __str__(self) :
        return f"{self.account_number} {self.balance} {self.date_of_opening} {self.customer_name}"

new = BankAccount("B001", 1000000, "10/8/2003", "Nguyen Huu Manh")
new.deposit(1000000)
new.withdraw(500000)
print(new)

