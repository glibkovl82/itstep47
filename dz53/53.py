# class Printer:
#     def does(self):
#         return "print"
# class Lamp:
#     def does(self):
#         return "glow"
# class Car:
#     def does(self):
#         return "ride"
# class Robot:
#     def __init__(self):
#         self.printer = Printer()
#         self.lamp = Lamp()
#         self.car = Car()
#     def do_it(self):
#         objs = [self.printer, self.lamp, self.car]
#         for item in objs:
#             print(item.does())
#
# robot = Robot()
# robot.do_it()




class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f'name = {self.name}, age = {self.age}')

class Student(Person):
    def __init__(self, name, age, id):
        super().__init__(name, age)
        self.id = id
    def study(self, subject):
        print(f'student {self.name}, id {self.id}, learn {subject}')
        print()
    def introduce(self):
        print(f'name = {self.name}, age = {self.age}, id {self.id},  {type(self)}')

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
    def teach(self, s):
        if not isinstance(s, Student):
            print("s is not class Student")
        else:
            print(f'Teacher {self.name}, teach subject {self.subject}, student {s.name}')
    def introduce(self):
        print(f'name = {self.name}, age = {self.age}, subject {self.subject},  {type(self)}')

class Employee(Person):
    def __init__(self, name, age, salary, specialty):
        super().__init__(name, age)
        self.salary = salary
        self.specialty = specialty
    def work(self):
        print(f"employee {self.name}, is {self.specialty} and has selery {self.salary} UAH")
        print()
    def introduce(self):
        print(f'name = {self.name}, age = {self.age}, specialty {self.specialty}, salary {self.salary}, {type(self)}')


p = Person("Jon", 18)
p.introduce()

s = Student("Jon", 18, "00000")
s.study("hisrory")

t = Teacher("Nina", 50, "geography")
t.teach(p)

w = Employee("Gregor", 40, 20000, "lawyer")
w.work()

s.introduce()
t.introduce()
w.introduce()




