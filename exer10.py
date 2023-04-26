"""
Exer 10

On this exercise we will be using the methods deposit() and withdraw() from exer7.py
Write two Unit Test classes, one for each class (BankAccount, StudentAccount)
and provide test cases that would check if they (methods) are working properly for different scenarios
"""

import unittest
from exer7 import BankAccount, StudentAccount

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount("Louis Miguel Pawaon", "123", 1000)

    def test_deposit(self):
        self.account.deposit(500)
        self.assertEqual(self.account.balance, 1500)

    def test_overdraft(self):
        self.account.withdraw(1500)
        self.assertEqual(self.account.balance, 1000)

    def test_withdraw(self):
        self.account.withdraw(500)
        self.assertEqual(self.account.balance, 500) 

class TestStudentAccount(unittest.TestCase):
    def setUp(self):
        self.account = StudentAccount("Julienne Andrea Panes", "456", 1500)

    def test_deposit(self):
        self.account.deposit(500)
        self.assertEqual(self.account.balance, 2000)

    def test_overdraft(self):
        self.account.withdraw(1500)
        self.assertEqual(self.account.balance, 1500)

    def test_withdraw(self):
        self.account.withdraw(400)
        self.assertEqual(self.account.balance, 1100)

if __name__ == '__main__':
    unittest.main()