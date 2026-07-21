import datetime
import pytz


class Account:
    """Simple account class with balance"""

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transction_list = [(Account._current_time(),balance)]
        print("Account created for " + self.name)
        self.show_balance()

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()
            self.transction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transction_list.append((Account._current_time(), -amount))
        else:
            print(
                "The amount must be greater than zero and no more then your account balance"
            )
        self.show_balance()

    def show_balance(self):
        print(f"Balance is {self.balance}")

    def show_transaction(self):
        for date, amount in self.transction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print(
                f"{amount:6} {tran_type} on {date} (local time was {date.astimezone()})"
            )


if __name__ == "__main__":
    Akhil = Account("Akhil", 0)
    Akhil.show_balance()

    Akhil.deposit(1000)
    # Akhil.show_balance()
    Akhil.withdraw(300)
    # Akhil.show_balance()
    Akhil.withdraw(500)

    Akhil.show_transaction()
    print()
    raj = Account("Raj", 800)
    raj.balance=300
    raj.deposit(100)
    raj.withdraw(200)
    raj.show_transaction()
    print(raj.__dict__)
    raj._Account__balance=40
    raj.show_balance()