# Practice
# 1.Write Python class named Circle constructed by radius and 2 methods which will compute area and perimeter of circle.
class Circle:
    """
     This class represents a circle object.

     Attributes:
         radius (float): The radius of the circle.
     """

    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:  # The area of a circle is pi times the radius squared (A = π r²)
        return 3.14 * self.radius ** 2

    def perimeter(self) -> float:  # perimeter of circle formula = 2 π r
        return 2 * 3.14 * self.radius


# 2.Write a Python program to crate two empty classes, Student and Marks. Create some instances and check whether they
# are instances of the said classes or not. Check if the said classes are subclasses of built-in object class or not
class Student:
    """
    This is an empty class representing a student object.
    """
    pass


class Marks:
    """
    This is an empty class representing a marks object.
    """
    pass


# Creation instances of the classes
student_name = Student()
marks_grade = Marks()

# Checking if the instances are of the said classes or not
print(isinstance(student_name, Student))
print(isinstance(marks_grade, Marks))

# Checking if the said classes are subclasses
print(issubclass(Student, object))
print(issubclass(Marks, object))


# Task 3. A Bank
class Account:
    def __init__(self, balance, account_number):
        self._balance = balance
        self._account_number = account_number

    @classmethod
    def create_account(cls, account_number):
        return cls(0.0, account_number)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError('Amount must be positive')

    def withdraw(self, amount):
        if amount > 0:
            self._balance -= amount
        else:
            raise ValueError('Amount must be positive')

    def get_balance(self):
        return self._balance

    def get_account_number(self):
        return self._account_number

    def __str__(self):
        return f'Account number: {self._account_number}, balance: {self._balance}'


class SavingsAccount(Account):
    """
    A class that represents a savings account.
    """

    def __init__(self, balance: float, account_number: int, interest_rate: float):
        super().__init__(balance, account_number)
        self._interest_rate = interest_rate

    def add_interest(self) -> None:
        interest = self._balance * self._interest_rate
        self._balance += interest

    def __str__(self) -> str:
        return f'Savings acc. number: {self._account_number}, balance: {self._balance}, int.rate: {self._interest_rate}'


class CurrentAccount(Account):
    """
    A class that represents a current account.
    """

    def __init__(self, balance: float, account_number: int, overdraft_limit: float):
        super().__init__(balance, account_number)
        self._overdraft_limit = overdraft_limit

    def send_overdraft_letter(self):
        if self._balance < 0:
            print(f"Sending overdraft letter for account {self._account_number}")

    def __str__(self) -> str:
        return f'Acc. number: {self._account_number},balance: {self._balance}, overdraft limit: {self._overdraft_limit}'


class Bank:
    """
    A class that represents a bank.
    """

    def __init__(self):
        """
        Initializes the Bank object with an empty list of accounts.
        """
        self._accounts = []

    def open_account(self, account: Account) -> None:  # Opens an account to the bank's list of accounts
        self._accounts.append(account)

    def close_account(self, account: Account) -> None:  # Removes an account from the bank's list of accounts
        self._accounts.remove(account)

    def pay_dividend(self, amount: float) -> None:  # Pays a dividend into each account in the bank's list of accounts
        for account in self._accounts:
            account.deposit(amount)

    def update(self) -> None:  # Updates each account in the bank's list of accounts.
        for account in self._accounts:
            if isinstance(account, SavingsAccount):
                account.add_interest()  # Adds interest
            elif isinstance(account, CurrentAccount):
                account.send_overdraft_letter()  # Send letters
