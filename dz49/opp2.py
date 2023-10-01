#          Н А С Л І Д У В А Н Н Я
# class Person:
#
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"
#
#     def info(self):
#         print("****2****")
#
# class Test:
#
#     def info(self):
#         print("!!!test!!!")
#
#
# class Student(Person, Test):
#
#     def __init__(self, first_name, last_name, school):
#         super().__init__(first_name, last_name)
#         self.scholl = school
#
#     def __str__(self):
#         return f"{self.first_name} {self.last_name} {self.scholl}"
#
#
#     def print_info(self):
#         print("----" *10)
#         super().info()
#         print(f"{self.first_name[0]}. {self.last_name}", end=' ')
#         print(self.scholl)
#
#
# s = Student("Jon", "Smith", "#3")
# print(s)
# s.print_info()
# mro = [x.__name__ for x in Student.__mro__]
# print(mro)


class Dog:

    def make_sound(self):
        print("Woof")


class Cat:

    def make_sound(self):
        print("Miaw")



d = Dog()
c = Cat()
d.make_sound()
c.make_sound()

def get_sound(x):
    x.make_sound()


print()
get_sound(d)
get_sound(c)



