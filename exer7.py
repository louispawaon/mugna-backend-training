"""
Exer 7

The following code defines the start of a class to represent bank accounts:

class BankAccount(object):
    interest_rate = 0.3

    def __init__(self,name,number,balance):
        self.name = name
        self.number = number
        self.balance = balance

Add instance methods called deposit() and withdraw() which increase and decrease the balance
of the account. make sure the withdraw() method doesn't allow the account to go into overdraft.
Add a third method called add_interest() which adds interest to the balnce (the interest should
be the interest rate multiplied by the current balance)

Create a subclass of BankAccount called StudentAccount.
Every StudentAccount should have an overdraft limit of 1000.
Write a constructor for the new class. Override the withdraw() method to make sure that 
students can withdraw money up to their overdraft limits.

"""
class BankAccount(object):
    interest_rate = 0.3

    def __init__(self,name,number,balance):
        self.name = name
        self.number = number
        self.balance = balance

    def deposit(self, amount):
        self.balance+=amount
        print(f"Successfully deposited {amount}, your new balance is {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Successfully withdrawn {amount}, your remaining balance is {self.balance}")
        else:
            print("Overdraft!")
    
    def add_interest(self):
        self.balance+=self.balance * BankAccount.interest_rate
        print(f"Your new balance is now {self.balance}")

class StudentAccount(BankAccount):
    overdraft_limit = 1000

    def withdraw(self, amount):
        if self.balance - amount >=StudentAccount.overdraft_limit:
            self.balance -= amount
            print(f"Student Account: Successfully withdrawn {amount}, your remaining balance is {self.balance}")
        else:
            print("Student Account: Overdraft!")

'''
#Test Users
Student1 = StudentAccount("Louis Pawaon", "1001", 1000)
Student1.deposit(500)
Student1.withdraw(500)

Person1 = BankAccount("Julienne Panes","2002",1000)
Person1.deposit(900)
Person1.withdraw(1000)
'''
    