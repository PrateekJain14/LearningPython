import pytz
import datetime


class Account:
    """Simple Account class with balance"""
    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self._balance = balance
        self._transaction_list = [(Account._current_time(), balance)]
        print("Account created for " + self._name)
        print("Initial balance is {}".format(self._balance))

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self.show_balance()
            self._transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            self._transaction_list.append((Account._current_time(), -amount))
        else:
            print("Amount must be greater than zero and not more than {}".format(self._balance))
        self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self._balance))

    def show_transaction(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                tran_type = "DEPOSITED"
            else:
                tran_type = "WITHDRAWN"
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))


if __name__ == "__main__":
    jim = Account("Jim", 0)
    jim.show_balance()

    jim.deposit(1000)
    jim.withdraw(500)
    jim.withdraw(2000)

    jim.show_transaction()
    jim.show_balance()

    steph = Account("steph", 800)
    steph.deposit(100)
    steph.withdraw(200)
    steph.show_transaction()
    steph.show_balance()
