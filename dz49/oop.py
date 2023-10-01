# class Person:
#     '''class Person виводить імена і рахунки людей'''
#
#     def __init__(self, name="xxx", money=0):
#         self.name = name
#         self.money = money
#         self.list_knowns = []
#         print("A new Person is born! = ", self.name)
#
#     def __str__(self):
#         return self.name + str(self.money)
#
#     def giveMoney(self, delta):
#         self.money += delta
#         print(f'Рахунок {self.name} поповнено на суму {delta}, всього = {self.money}')
#
#     def know(self, person):
#         self.list_knowns.append(person)
#
#
# A = Person()
# B = Person()
# C = Person("Petro", 10)
# D = Person("ira", 30)
# A.know(C)
# A.know(D)
# print("list of knowns:", [person.name for person in A.list_knowns])
#
# print(f"Tom: Name = {A.name}, money = {A.money:.2f}")
# print(f"Tom: Name = {B.name}, money = {B.money:.2f}")
#
# A.name = "Ivan"
# B.name = "Anna"
# B.money = 100.2852
#
# A.giveMoney(50.127)
# B.giveMoney(40)
# C.giveMoney(100)
# D.giveMoney(100)
#
#
# print(f"Tom: Name = {A.name}, money = {A.money:.2f}")
# print(f"Tom: Name = {B.name}, money = {B.money:.2f}")
# print(f"Tom: Name = {C.name}, money = {C.money:.2f}")
# print(f"Tom: Name = {D.name}, money = {D.money:.2f}")
# def info(person):
#     i = person.name + str(person.money)
#     return i
# people = [A, B, C, D]
# for p in people:
#    print(p)
# # help(Person)
# print(Person.__doc__)



#          Н А С Л І Д У В А Н Н Я
class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name



    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Baby(Person):

    def speak(self):
        print(f"{self.first_name} says: Blah blah blah")

class Adult(Person):

    def speak(self):
        print(f"My name is {self.first_name} ")

class BetterPerson(Person):
    @property
    def full_name(self):
        return f"{self.first_name}___ {self.last_name}"

p = BetterPerson("Jon", "Kirby")
b = Baby("Ivan", "Smith")
a = Adult("Alice", "Stoun")
print(p.full_name)

# print(p, isinstance(p, Person))
# print(b, isinstance(b, Baby))
b.speak()
a.speak()