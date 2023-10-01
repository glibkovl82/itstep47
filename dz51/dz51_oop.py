class BankAccount:

    def __init__(self, account_number, balance, owner_name):
        self.__account_number = account_number
        self._balance = balance
        self.owner_name = owner_name

    def __str__(self):
        return f'{self.owner_name}, account: {self.__account_number}, balance: {self._balance}'

    def deposit(self, add):
        self._balance += add
        print(f"Balance after add: {self._balance} grn")

    def withdraw(self, withdrawing_money):
        self._balance -= withdrawing_money
        print(f"Balance after withdrawing: {self._balance} grn")

    def change_owner_name(self, new_name):
        self.owner_name = new_name

    def display_account_info(self):
        print(f'{self.owner_name}: account {self.__account_number}, balance {self._balance}')

    def transfer(self, client2, transfer_money):
        print(f'balance client1 befor transfer: {self._balance}, balance client2 - {client2} ')
        if not isinstance(transfer_money, (int, float)):
            print("Сума переказу повинна бути числом 'int' або 'float'")
        else:
            if self._balance >= transfer_money:
                try:
                    if transfer_money <= 0:
                        raise ValueError("Сума переказу повинна бути більша за '0'")
                    self._balance -= transfer_money
                    client2 += transfer_money
                    print(f'Переказ {transfer_money} grn пройшов успішно\nbalance client1 after transfer: {self._balance}, balance client2: {client2}')
                except TypeError as e:
                    print(e, "Сума переказу повинна бути числом 'int' або 'float'")
                except ValueError as v:
                    print(ValueError, v)
            else:
                print("Для переказу недестатньо коштів на рахунку")
    @staticmethod
    def check_account_number(account_numb):
        if 10000 <= account_numb < 100000:
            print(f'account {account_numb} is valid')
        else:
            print(f'account {account_numb} is not valid (account number must consist of 5 digits)')
    #
    def get_account_number(self):
        return self.__account_number

    def set_account_number(self, new_account_number):
        self.__account_number = new_account_number
        return self.__account_number

    @property
    def account_number(self):
        return self.__account_number

    @account_number.setter
    def account_number(self, new_account_number):
        self.__account_number = new_account_number


costomer1 = BankAccount(99999, 100, "Jhon")
costomer2 = BankAccount(888888, 500, "Luck")
costomer3 = BankAccount(77777, 700, "Frenk")
costomer4 = BankAccount(66666, 900, "Sten")
print(f'{costomer1}\n{costomer2}\n{costomer3}\n{costomer4}')
print()
costomer1.deposit(500)
print(costomer1)
costomer1.withdraw(200)
costomer4.deposit(600)
print(costomer4)

costomer1.change_owner_name("Lee")
print(costomer1)
print()

costomer1.display_account_info()
print()

costomer1.transfer(costomer2._balance, 100)
print()
BankAccount.check_account_number(costomer1.account_number)
costomer2.check_account_number(costomer2.account_number)
print()
print(f'current account number {costomer3.owner_name} - {costomer3.get_account_number()}')
print()
print(f'new account number {costomer3.owner_name} - {costomer3.set_account_number(11111)}')
print()
print('current account number', costomer4.owner_name, "-", costomer4.account_number)
print()
costomer4.account_number = 22222
print('new account number', costomer4.owner_name, "-", costomer4.account_number)
