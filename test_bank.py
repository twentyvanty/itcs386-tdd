# test_bank.py 
import pytest 
from bank import BankAccount, InsufficientFunds 
@pytest.fixture 
def account(): 
 return BankAccount("alice", balance=100) 
def test_deposit_increases_balance(account): 
 account.deposit(50) 
 assert account.balance == 150 
def test_withdraw_more_than_balance_is_refused(account): 
 with pytest.raises(InsufficientFunds): 
  account.withdraw(500) 
 assert account.balance == 100 
def test_each_test_gets_a_fresh_account(account): 
 assert account.balance == 100 
 def test_zero_deposit_is_rejected():
        account = BankAccount()

        with pytest.raises(ValueError):
         account.deposit(0)
 

def test_withdrawing_whole_balance_leaves_zero():
    account = BankAccount()
    account.deposit(100)

    account.withdraw(100)

    assert account.balance == 0


def test_two_withdrawals_both_reduce_balance():
    account = BankAccount()
    account.deposit(100)

    account.withdraw(20)
    balance_after_first = account.balance

    account.withdraw(30)

    assert account.balance < balance_after_first
    assert balance_after_first < 100

def test_interest(account): 
 account.add_interest(0.10) 
 assert account.balance == 110

