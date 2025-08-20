# -*- coding: utf-8 -*-
#Курс: AI+Python
# Модуль 11. ООП
# Тема: ООП. Частина 1
#  Завдання 1
# Створіть клас Student з атрибутами name та age. Додайте
# метод для виводу інформації у форматі «Ім’я: {name}, вік:
# {age}»


class Student:
    """ Клас Student"""
    def __init__(self,name='',age=0):
        self.name : str = name
        self.age : int = age

    def show(self):
        return f"Ім’я: {self.name}, вік:  {self.age}"


# Завдання 2
# Створіть список з 3-ма студентами, дані вводить
# користувач. Після чого для кожного студента виведіть
# інформацію про нього за допомогою метода.

students :list[Student]= []
students.append(Student())
students.append(Student())
students.append(Student())

for index,stud in enumerate(students):
    stud.name = input("Name? ")
    stud.age = input("Age? ")

    print(students[index].show())


# Завдання 3
# Створіть клас Circle з атрибутом radius. Додайте метод для
# отримання площі кола
class Circle:
    pass


# Завдання 4
# Створіть клас BankAccount з атрибутами owner та balance.
# Додайте метод deposit для поповнення рахунку
# Додайте метод withdraw для зняття грошей з рахунку
# Додайте метод info для виведення інформації про баланс
# Завдання 5
# Створіть клас Car з атрибутами brand(марка), year(рік
# випуску), is_ready(чи готовий до поїздки, за замовчування
# False).
# Додайте метод start_engine який заводить двигун, і змінює
# атрибут is_ready
# Додайте метод move який виводить повідомлення, що
# автомобіль їде, або ж ще не готовий в залежності від is_ready.
