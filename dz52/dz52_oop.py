import json, os
import requests
class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __str__(self):
        return f'{self.amount}, {self.currency}'

class BankAccount:
    accounts = []
    balances = []
    exchange_rate = {}
    obj_1 = []

    def __init__(self, account_number, balance, owner_name, currency):
        self.__account_number = account_number
        self._balance = Money(balance, currency)
        self.owner_name = owner_name
        self.accounts.append(self)
        self.balances.append(self._balance.amount)
        self.obj_1.append({"account_number": self.get_account_number(), "balance": self._balance.amount, "currency": self._balance.currency, "name": self.owner_name})

    def __str__(self):
        return f'{self.owner_name}, account: {self.__account_number}, balance: {self._balance}'

    @classmethod
    def create_exchange_rate(cls):
        name_path = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
        response = requests.get(name_path)
        rates = json.loads(response.text)
        cls.exchange_rate = {v['cc']: v["rate"] for v in rates}
        cls.exchange_rate["UAH"] = 1

    def deposit(self, add):
        self._balance.amount += add
        print(f"Balance {self.owner_name}, account_number {self.__account_number} after add: {self._balance.amount:.2f} {self._balance.currency}")

    def withdraw(self, withdrawing_money):
        self._balance.amount -= withdrawing_money
        print(f"Balance after withdrawing: {self._balance}")

    def change_owner_name(self, new_name):
        self.owner_name = new_name

    def display_account_info(self):
        print(f'{self.owner_name}: account {self.__account_number}, balance {self._balance}')

    def transfer(self, client2, transfer_money, currency):
        print(f'befor transfer: {self.owner_name}, account_number-{self.__account_number}, balance-{self._balance}\nbefor transfer: {client2.owner_name}, account_number-{client2.__account_number}, balance-{client2._balance}')
        if not isinstance(transfer_money, (int, float)):
            raise TypeError("Сума переказу повинна бути числом 'int' або 'float'")
        elif transfer_money <= 0:
            raise ValueError("Сума переказу повинна бути більша за '0'")
        else:
            if self._balance.amount > transfer_money:
                if self._balance.currency == client2._balance.currency:
                    self._balance.amount -= transfer_money
                    client2.deposit(transfer_money)
                    print(f'Переказ {transfer_money} {currency} пройшов успішно\n\
after transfer: {self.owner_name}, account_number-{self.__account_number}, balance-{self._balance}')
                else:
                    self._balance.amount -= transfer_money
                    change_money = self.transfer_funds(client2._balance.currency, transfer_money)
                    client2.deposit(change_money)
                    print(f'Переказ {transfer_money} {currency} пройшов успішно\n\
balance client1 {self.owner_name}, account_number {self.__account_number} after transfer: {self._balance}')
            else:
                print("Для переказу недестатньо коштів на рахунку")

    def transfer_funds(self, cur, transfer_money):
        if cur == "USD": # перевід в доллари
            r = self.exchange_rate["USD"] / self.exchange_rate[cur]
            return transfer_money / r

        elif self._balance.currency == "USD": # перевід з долларів в іншу валюту
            r = self.exchange_rate["USD"] / self.exchange_rate[cur]
            return transfer_money * r
        else:
            if self.exchange_rate[self._balance.currency] < self.exchange_rate["USD"]:
                r = self.exchange_rate["USD"] / self.exchange_rate[self._balance.currency] # коефіцієнт валюти клієнта 1 до доллара
                r2 = transfer_money / r # перевід валюти клієнта 1 в доллари
                r3 = self.exchange_rate["USD"] / self.exchange_rate[cur] #коефіцієнт валюти клієнта 2 до доллара
                return r2 * r3 # перевід з доллара у валюту клієнта 2
            else:
                r = self.exchange_rate[self._balance.currency] / self.exchange_rate["USD"]  # коефіцієнт доллара до валюти клієнта 1
                r2 = transfer_money * r  # перевід валюти клієнта 1 в доллари
                if self.exchange_rate["USD"] > self.exchange_rate[cur]:
                    r3 = self.exchange_rate["USD"] / self.exchange_rate[cur]  # коефіцієнт валюти клієнта 2 до доллара
                    return r2 * r3  # перевід з доллара у валюту клієнта 2
                else:
                    r3 = self.exchange_rate[cur] / self.exchange_rate["USD"]  # коефіцієнт валюти клієнта 2 до доллара
                    return r2 / r3


    @staticmethod
    def check_account_number(account_numb):
        if 10000 <= account_numb < 100000:
            print(f'account {account_numb} is valid')
        else:
            print(f'account {account_numb} is not valid (account number must consist of 5 digits)')

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

    @classmethod
    def find_accounts_by_owner(cls, owner_name):
        maching_accounts = []
        for account in cls.accounts:
            if account.owner_name == owner_name:
                maching_accounts.append(account)
        return maching_accounts

    @classmethod
    def get_average_balance(cls):
        return sum(cls.balances) / len(cls.balances)

    @classmethod
    def save_account(cls):
        with open("account_number.json", mode="w") as file:
            json.dump(cls.obj_1, file, indent=4)
            print("done")


    def save_acoount_2(self):
        self.account_save = {"account_number": self.get_account_number(),
                     "balance": self._balance.amount,
                     "currency": self._balance.currency,
                     "name": self.owner_name}
        path = "data/account_" + self.owner_name + ".json"
        with open(path, mode="w") as file2:
            json.dump(self.account_save, file2, indent=4)

    def delete_account(self):
        path = "data/account_" + self.owner_name + ".json"
        os.remove(path)
        del self.owner_name
        del self.__account_number
        del self._balance

if __name__ == "__main__":
    costomer1 = BankAccount(99999, 100, "Jhon", "UAH")
    costomer2 = BankAccount(88888, 500, "Luck", "UAH")
    costomer3 = BankAccount(77777, 700, "Frenk", "PLN")
    costomer4 = BankAccount(66666, 900, "Sten", "TRY")
    print(f'{costomer1}\n{costomer2}\n{costomer3}\n{costomer4}')

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

    # costomer1.transfer(costomer2._balance, 100)
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
    print()
    costomer5 = BankAccount(18181, 1000, "Cros", "TRY")
    costomer6 = BankAccount(16161, 1600, "Cris", "GBP")
    costomer7 = BankAccount(17171, 1700, "Graf", "EUR")
    lst = BankAccount.find_accounts_by_owner("Cros")
    lst1 = BankAccount.find_accounts_by_owner("Cris")
    lst2 = BankAccount.find_accounts_by_owner("Graf")
    
    print()
    print([x.owner_name for x in BankAccount.accounts])
    print()
    print(f'avg balance: {BankAccount.get_average_balance():.2f}')
    BankAccount.create_exchange_rate()
    costomer1.transfer(costomer2, 50, "UAH")
    costomer1.save_account()
    costomer1.save_acoount_2()
    costomer2.save_acoount_2()
    costomer7.save_acoount_2()
    costomer7.delete_account()
    costomer4.transfer(costomer3, 100, "TRY")
    print()
    costomer6.transfer(costomer5, 100, "GBP")


