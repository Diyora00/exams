from typing import Optional
from colorama import Fore
# Baxtiyorova Diyora
# Variant B
# Task - 1
print(Fore.LIGHTBLUE_EX, "Task - 1 ---------------------------------------", Fore.RESET)


class Phone:
    def __init__(self, name: Optional[str] = None, color: Optional[str] = None,
                 price: Optional[float] = 0):
        self.name = name
        self.color = color
        self.price = price

    def get_name(self):
        print('Name: ' + self.name)

    def get_price(self):
        print('Price: ' + str(self.price))


try:
    name1 = str(input('Enter name of the phone: '))
    price1 = float(input('Enter price: '))
except ValueError as e:
    print(e)
else:
    phone = Phone(name1, price=price1)
    phone.get_name()
    phone.get_price()


print(Fore.LIGHTBLUE_EX, "Task - 2 ---------------------------------------", Fore.RESET)


# Task - 2
class Animal:
    def __init__(self, name: Optional[str] = None, age: Optional[int] = 0,
                 sound: Optional[str] = None, id_a: Optional[int] = None):
        self.name = name
        self.__age = age
        self.sound = sound
        self.__id_a = id_a

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, other):
        self.__age = other

    @property
    def id_a(self) -> int:
        return self.__id_a

    @id_a.setter
    def id_a(self, other):
        self.__id_a = other


try:
    other_age = int(input('Enter animal\'s age: '))
except ValueError as e:
    print(e)
else:
    animal1 = Animal('Bear')
    animal1.age = other_age
    print('Animal\'s age: ', animal1.age)


print(Fore.LIGHTBLUE_EX, "Task - 3 ---------------------------------------", Fore.RESET)


# Task - 3
class Grandfather:
    def __init__(self, name: Optional[str] = None):
        self.name = name
        self.occupation = 'pilot'

    def work(self):
        print(f'Grandfather worked as a {self.occupation}')


class Father(Grandfather):
    def __init__(self, name: Optional[str] = None):
        self.name = name
        self.talent = 'fast remembering'
        super().__init__(name)

    def talent_f(self):
        print(f'Father\'s talent is {self.talent}')


class Son(Father):
    def __init__(self, name: Optional[str] = None):
        self.name = name
        super().__init__(name)


son = Son('Peter')
son.work()
son.talent_f()
print(son.occupation)


print(Fore.LIGHTBLUE_EX, "Task - 4 ---------------------------------------", Fore.RESET)


# Task - 4
# Polymorphism
class Person:
    def __init__(self, name: Optional[str] = None, age: Optional[int] = 0):
        self.name = name
        self.age = age

    def get_info(self):
        print(f'Name: {self.name}, Age: {self.age}')


class Student(Person):
    def __init__(self, name: Optional[str] = None, age: Optional[int] = None):
        super().__init__(name, age)

    def get_info(self):
        print(f'Name: {self.name}, Age: {self.age}')


try:
    n1 = str(input('Enter name of the person: '))
    a1 = int(input('Enter age of the person: '))
    n2 = str(input('Enter name of the student: '))
    a2 = int(input('Enter age of the student: '))
except ValueError as e:
    print(e)
else:
    p1 = Person(n1, a1)
    s1 = Student(n2, a2)
    p1.get_info()
    s1.get_info()
