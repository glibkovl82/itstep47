#             Домашня робота №50 ООП. Створення найпростіших класів.
    # Завдання 1.
    # Створіть клас Circle (Коло) із конструктором (метод __init__),
    # у якому вказується його радіус, по замовчуванню він дорівнює 1.
    # Реалізуйте метод  __str__ (або__repr__), що повертає рядкове
    # представлення для друку даного об’єкта.
# Визначити такі методи:
# - метод для обчислення площі круга.
# - метод для обчислення довжини кола
# Перевірити і заскрінити роботу програми:
# - створити один об’єкт (екземпляр) класу - коло з
#   радіусом 2, а другий – з радіусом 3.
# - роздрукувати ці об’єкти кола за допомогою print
# - викликати метод для обчислення площі круга для першого кола.
# - викликати метод для обчислення довжини кола для іншого кола.

from math import pi
class Circle:

    def __init__(self, circ=1):
        self.circ = circ

    def __str__(self):
        return f'Circle radius {self.circ}'

    def length_circle(self):
        return self.circ * 2 * pi

    def sqare_circle(self):
        return self.circ ** 2 * pi


a1 = Circle()
print(a1)
print()
a2 = Circle(2)
a3 = Circle(3)
print(f'{a2}\n{a3}')
print()
print(f'length of circle a1 = {a1.length_circle():.2f}')
print(f'sqare of circle a1 = {a1.sqare_circle():.2f}')
print()
print(f'length of circle a2 = {a2.length_circle():.2f}')
print(f'sqare of circle a2 = {a2.sqare_circle():.2f}')
print()
print(f'length of circle a3 = {a3.length_circle():.2f}')
print(f'sqare of circle a3 = {a3.sqare_circle():.2f}')


