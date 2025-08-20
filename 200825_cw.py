# -*- coding: utf-8 -*-
#Курс: AI+Python
# Модуль 11. ООП
# Тема: ООП. Частина 1
#  Завдання 1
# Створіть клас Student з атрибутами name та age. Додайте
# метод для виводу інформації у форматі «Ім’я: {name}, вік:
# {age}»
import math
import random


# class Student:
#     """ Клас Student"""
#     def __init__(self,name='',age=0):
#         self.name : str = name
#         self.age : int = age
#
#     def show(self):
#         return f"Ім’я: {self.name}, вік:  {self.age}"
#
# #
# # # Завдання 2
# # # Створіть список з 3-ма студентами, дані вводить
# # # користувач. Після чого для кожного студента виведіть
# # # інформацію про нього за допомогою метода.
# #
# # students :list[Student]= []
# # students.append(Student())
# # students.append(Student())
# # students.append(Student())
# #
# # for index,stud in enumerate(students):
# #     stud.name = input("Name? ")
# #     stud.age = input("Age? ")
# #
# #     print(students[index].show())
#
#
# # Завдання 3
# # Створіть клас Circle з атрибутом radius. Додайте метод для
# # отримання площі кола
# class Circle:
#     def __init__(self, radius):
#         self.radius: float = radius
#
#     def calculate_square(self):
#         return math.pi * (self.radius ** 2)
#
#
# с1=Circle(radius=4.4)
# print(с1.calculate_square())
#
#
#
# # Завдання 4
# # Створіть клас BankAccount з атрибутами owner та balance.
# # Додайте метод deposit для поповнення рахунку
# # Додайте метод withdraw для зняття грошей з рахунку
# # Додайте метод info для виведення інформації про баланс
# class BankAccount:
#     """
#     Represents a bank account with an owner and related functionality.
#
#     The BankAccount class encapsulates the details of a bank account including
#     its owner and any associated operations such as deposits, withdrawals, and
#     balance inquiries.
#
#     :type owner: Student
#     :type balance: float
#     """
#     def __init__(self, owner:Student=Student(), balance=0.0 ):
#         self.owner : Student = owner
#         self.balance : float = balance
#
#     # метод deposit для поповнення рахунку
#     def deposit(self, deposit_suma:float=0.0):
#         self.balance += deposit_suma
#
#     # метод withdraw для зняття грошей з рахунку
#     def withdraw(self, withdraw_suma:float=0.0):
#         self.balance -= withdraw_suma
#
#     # метод info для виведення інформації про баланс
#     def info(self):
#         return f"Власник{self.owner.name}({self.owner.age}) Баланс:{self.balance}"
#
#
# students :list[Student]= []
# students.append(Student())
# students.append(Student())
# students.append(Student())
#
# for index,stud in enumerate(students):
#     stud.name = input("Name? ")
#     stud.age = input("Age? ")
#
#     print(students[index].show())
#
#     b1=BankAccount(students[index], 0.0)
#     amount = round(random.uniform(10.0, 1000.0), 2)
#     amount2 = round(random.uniform(10.0, 1000.0), 2)
#
#     print(b1.info())
#     b1.deposit(amount)
#     print(b1.info())
#     b1.withdraw(amount2)
#     print(b1.info())

# Завдання 5
# Створіть клас Car з атрибутами brand(марка), year(рік
# випуску), is_ready(чи готовий до поїздки, за замовчування
# False).
# Додайте метод start_engine який заводить двигун, і змінює
# атрибут is_ready
# Додайте метод move який виводить повідомлення, що
# автомобіль їде, або ж ще не готовий в залежності від is_ready.
class Car:
    def __init__(self, brand, year, is_ready=False):
        self.brand = brand
        self.year = year
        self.is_ready = is_ready

    def start_engine(self):
        self.is_ready = True

    def move(self):
        if self.is_ready:
            print(f"Автомобіль {self.brand} їде")
        else:
            print(f"Автомобіль {self.brand} ще не готовий")


# --- Перевірка роботи класу Car ---
def test_car():
    print("\n=== Перевірка Car ===")
    car = Car("Toyota", 2020)
    # Початковий стан
    assert car.is_ready is False, "Початково авто має бути не готове"
    car.move()  # очікуємо повідомлення, що ще не готовий

    # Після запуску двигуна
    car.start_engine()
    assert car.is_ready is True, "Після start_engine авто має бути готове"
    car.move()  # очікуємо повідомлення, що авто їде
    print("Перевірка пройшла успішно.")

if __name__ == "__main__":
    test_car()

