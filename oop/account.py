#!/usr/bin/env python


class Account:
    def __init__(self, name="default_account", start_balance=0):
        self.__name = name
        self.__start_balance = start_balance
        self.__transactions = []

    def __str__(self):
        return f"{self.__name} account - balance: {self.balance}"

    ## Validation method to check incoming values are integers
    def __validate(self, value):
        if not isinstance(value, int):
            raise ValueError("please use an integer value")

    ## Properties
    @property
    def start_balance(self):
        return self.__start_balance

    @property
    def balance(self):
        return self.__start_balance + sum(self.__transactions)

    ## Dunders
    def __len__(self):
        return len(self.__transactions)

    ## List/Iterator dunders
    def __iter__(self):
        return iter(self.__transactions)

    def __setitem__(self, index, value):
        self.__transactions[index] = value

    def __getitem__(self, index):
        return self.__transactions[index]

    ## Comparison dunders to allow Account instance boolean comparisons
    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    ## Binary dunders for transactions applied to Account instances
    def __add__(self, amount):
        self.__validate(amount)
        self.__transactions.append(amount)

    def __sub__(self, amount):
        self.__validate(amount)
        self.__transactions.append(-amount)

    ## Context Manager dunders
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print(f"exc_type: {exc_type}")
            print(f"exc_value: {exc_value}")
            print(f"exc_traceback: {traceback}")
