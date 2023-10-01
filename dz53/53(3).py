import datetime
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
class Baby(Person):
    def speak(self):
        print("Hi, I'm", self.first_name)
class Adult(Person):
    def speak(self):
        print("Hello my name is", self.first_name)

class Calendar:
    def book_appointment(self, date):
        print("Booking appointment for date", date)

class OrganizedAdult(Adult, Calendar):
    def book_appointment(self, date):
        print('Note that you are booking an appointment.')
        super().book_appointment(date)

class OrganizedBaby(Baby, Calendar):
    def book_appointment(self, date):
        print('Note that you are booking an appointment with a baby.')
        super().book_appointment(date)
#

stive = OrganizedBaby('Stive', 'Brook')
jhon = OrganizedAdult('Jhon', 'Brook')

jhon.speak()
jhon.book_appointment(datetime.date(2023,9,29))

stive.speak()
stive.book_appointment(datetime.date(2023,9,28))
