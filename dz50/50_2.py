#             Домашня робота №50 ООП. Створення найпростіших класів.
# Завдання 2.
# - Реалізуйте клас Car (Автомобіль) із такими властивостями-атрибутами:
# назва моделі, рік випуску, виробник, об’єм двигуна, колір машини, ціна.
# - Реалізуйте конструктор __init__ для класу та метод __str__.
# - Реалізуйте метод для зміни кольору машини.
# - Реалізуйте метод для зміни ціни машини.
# - Додайте атрибут (поле) total класу, у якому буде міститись
# сумарна кількість створених об’єктів-автомобілів у програмі.
# - Реалізуйте метод, який через об’єкт повертає значення атрибуту
# total класу Car.
#  На кожному кроці протестуйте виконання.

class Car:
    total = 0

    def __init__(self, model, year, maker, engine, color, price=1000):
        self.model = model
        self.year = year
        self.maker = maker
        self.engine = engine
        self.color = color
        self.price = price
        Car.total += 1

    def __str__(self):
        return (f"model: {self.model}, \
graduation year: {self.year}, \
maker: {self.maker}, \
engine: {self.engine}, \
color: {self.color}, \
price: {self.price}")

    def change_color(self, new_color):
        self.color = new_color
        print(f"model: {self.model}, \
graduation year: {self.year}, \
maker: {self.maker}, \
engine: {self.engine}, \
color: {self.color}, \
price: {self.price}")

    def change_price(self, new_price):
        self.price = new_price
        print(f"model: {self.model}, \
graduation year: {self.year}, \
maker: {self.maker}, \
engine: {self.engine}, \
color: {self.color}, \
price: {self.price}")

    def get_count_car(self):
        return Car.total


c = Car("X5", 2005, "BMW", 2.5, "black", 25000)
c1 = Car("Lanos", 2002, "Deawoo", 1.5, "green", 3000)
c2 = Car("Pejout", 2014, "308sw", 1.6, "wight", 8000)
print(f'{c}\n{c1}\n{c2}')
print()
c.change_color("silver")
c2.change_price(2000)
c1.change_color("yellow")
print()
print(f'Count created cars: {c.get_count_car()}')



