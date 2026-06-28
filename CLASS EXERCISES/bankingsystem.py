class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def show_balance(self):
        print(f"{self.owner}'s balance: ${self.balance:.2f}")


class Transaction:
    def __init__(self, account):
        self.account = account

    def process(self, amount, target=None):
        raise NotImplementedError("Subclasses must implement this method")


class Deposit(Transaction):
    def process(self, amount, target=None):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.account.balance += amount
        print(f"{self.account.owner} deposited ${amount:.2f}")
        return self.account.balance


class Withdrawal(Transaction):
    def process(self, amount, target=None):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.account.balance:
            raise ValueError("Insufficient funds")
        self.account.balance -= amount
        print(f"{self.account.owner} withdrew ${amount:.2f}")
        return self.account.balance


class Transfer(Transaction):
    def process(self, amount, target=None):
        if target is None:
            raise ValueError("A recipient account is required for transfer")
        if amount <= 0:
            raise ValueError("Transfer amount must be positive")
        if amount > self.account.balance:
            raise ValueError("Insufficient funds")

        self.account.balance -= amount
        target.balance += amount
        print(f"{self.account.owner} transferred ${amount:.2f} to {target.owner}")
        return self.account.balance, target.balance


if __name__ == "__main__":
    employer = BankAccount("Employer", 1000.00)
    employee = BankAccount("Employee", 200.00)

    print("Initial balances")
    employer.show_balance()
    employee.show_balance()
    print()

    # Method overloading is shown by using the same process method with
    # different inputs: amount only for deposit/withdrawal and amount+target for transfer.
    deposit = Deposit(employer)
    deposit.process(500.00)

    withdrawal = Withdrawal(employer)
    withdrawal.process(200.00)

    transfer = Transfer(employer)
    transfer.process(150.00, employee)

    print()
    print("Updated balances")
    employer.show_balance()
    employee.show_balance()
