class BankAccount:

    def __init__(self, name, balance, currency):
        self.__name = name
        self.__balance = balance
        self.__currency = currency
        self.__history = ['Account was created']

    def deposit(self, amount):
        self.__balance += amount
        self.__history.append('Deposited {}{}'.format(amount, self.__currency))

    def balance(self):
        self.__history.append('Balance check -> {}{}'.format(self.__balance, self.__currency))
        return self.__balance 

    def name(self):
        return self.__name

    def withdraw(self, amount):
        if amount > self.__balance:
            self.__history.append("Withdraw for {}{} failed".format(amount, self.__currency))
            return False
        else:
            self.__balance -= amount
            self.__history.append("{}{} was withdrawed".format(amount, self.__currency))
            return True

    def get_currency(self):
        return self.__currency

    def __str__(self):
        return "Bank account for {} with balance of {}{}".format(self.__name, self.__balance, self.__currency)

    def __int__(self):
        self.__history.append('__int__ check -> {}{}'.format(self.__balance, self.__currency))
        return self.__balance

    def transfer_to(self, account, amount):
        if self.__currency == account.get_currency():
            if self.withdraw(amount):
                account.deposit(amount)
                self.__history.append("Transfer to {} for {}{}".format(account.name(), amount, account.get_currency()))
                account.history().append("Transfer from {} for {}{}".format(self.name(), amount, account.get_currency()))
                return True
        return False

    def history(self):
        return self.__history
