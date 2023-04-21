# 1. Write a test for the Bank class that we wrote in 15 lesson (github.com/moveol/pjct_python_hw/blob/main/OM_hw_15.py)
# You should write a test for the open_account method.
# Ensure that the account is opened and has balance.

import unittest
from bank import Bank, Account, SavingsAccount, CurrentAccount


class TestBank(unittest.TestCase):
    def setUp(self):
        self.bank = Bank()

    def test_open_account(self):
        account_number = 1234567890
        account = Account.create_account(account_number)
        initial_balance = 100.0

        # Ensure the account is not in the bank's accounts list
        self.assertNotIn(account, self.bank._accounts)

        # Open the account and deposit initial balance
        self.bank.open_account(account)
        account.deposit(initial_balance)

        # Ensure the account is now in the bank's accounts list
        self.assertIn(account, self.bank._accounts)

        # Ensure the account has the correct balance
        self.assertEqual(account.get_balance(), initial_balance)


if __name__ == '__main__':
    unittest.main()

# 2. Test update method. It should check that code added interest and sended a message (print function was called).


def test_update(self):
    savings_account = SavingsAccount(100.0, 1234567890, 0.05)
    current_account = CurrentAccount(-100.0, 1234567891, 500.0)
    self.bank.open_account(savings_account)
    self.bank.open_account(current_account)

    # Ensure that add_interest method is called on the SavingsAccount
    with unittest.mock.patch.object(SavingsAccount, 'add_interest') as mock_method:
        self.bank.update()
        mock_method.assert_called_once()

    # Ensure that send_overdraft_letter method is called on the CurrentAccount
    with unittest.mock.patch.object(CurrentAccount, 'send_overdraft_letter') as mock_method:
        self.bank.update()
        mock_method.assert_called_once()

    # Ensure that the accounts' balances have been updated
    self.assertEqual(savings_account.get_balance(), 105.0)
    self.assertEqual(current_account.get_balance(), -100.0)
