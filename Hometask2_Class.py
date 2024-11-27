# Задача 1. Создание класса "Книга"
# Создайте класс Book с полями:
# title (название книги, тип String),
# author (автор, тип String),
# price (цена, тип double).
# Реализуйте:
# Конструктор, который принимает все поля.
# Геттеры и сеттеры для каждого поля.
# В методе main создайте объект класса Book, измените через сеттеры автора и цену, а затем выведите в консоль информацию о книге.
class Book():
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        
    def print_info(self):
        return(f'Название книги {self.title}, цена {self.price}, автор - {self.author}')

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if not value.strip():
            raise ValueError("Название книги не может быть пустым значением")
        self._title = value
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if not value.strip():
            raise ValueError('Автор не может быть пустым значением')
        self._author = value
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Цена не может быть отрицательным полем")
        self._price = value
           
# book1 = Book('1984', 'Дж. Оруэлл', 500)
# book2 = Book('1', '2', 3)
# book2.price = 400
# book2.author = 'С. Довлатов'
# book2.title = 'Заповедник'
# print(book1.print_info())
# print(book2.print_info())

# Задача 2. Класс "Человек"
# Создайте класс Person с полями:
# name (имя, тип String),
# age (возраст, тип int),
# gender (пол, тип String).
# Реализуйте:
# Конструктор с параметрами name и age.
# Конструктор по умолчанию (без параметров).
# Геттеры и сеттеры.
# Добавьте метод printInfo(), который выводит информацию о человеке в формате:
# Имя: <name>, Возраст: <age>, Пол: <gender>
# В методе main создайте несколько объектов класса Person, вызовите метод printInfo() для каждого объекта.

# class Person():
#     def __init__(self, name=None, age=None, gender=None):
#         self._name = name
#         self._age = age
#         self._gender = gender
        
#     def printInfo(self):
#         print(f'Имя: {self.name}, Возраст: {self.age}, Пол: {self.gender}')

#     @classmethod
#     def with_name_and_age(cls, name, age):
#         return cls(name = name, age = age)

#     @property
#     def name(self):
#         return self._name

#     @name.setter
#     def name(self, value):
#         if not value.strip() or not isinstance(value, str):
#             raise ValueError("Имя не может быть пустым")
#         self._name = value

#     @property
#     def age(self):
#         return self._age

#     @age.setter
#     def age(self, value):
#         if value < 0 or not isinstance(value, int):
#             raise ValueError("Возраст должен быть положительным")
#         self._age = value 

#     @property
#     def gender(self):
#         return self._gender
    
#     @gender.setter
#     def gender(self, value):
#         if value is not None and (not isinstance(value, str) or not  value.strip()):
#             raise ValueError("Пол не может быть пустым")
#         self._gender = value

# тестирование (вместо метода мейн)
# try:
#     # использую конструктор по умолчанию
#     person1 = Person()
#     person1.name = "1"      
#     person1.age = 21
#     person1.gender = "Мужчина"
#     person1.printInfo()

#     # использую конструктор другой
#     person2 = Person.with_name_and_age("Мария", 30)
#     person2.gender = "женщина"
#     person2.printInfo()
# except ValueError as e:
#     print(e)

# Задача 3. Класс "Машина"
# Создайте класс Car с полями:
# brand (бренд, тип String),
# model (модель, тип String),
# year (год выпуска, тип int),
# price (цена, тип double).
# Реализуйте:
# Конструктор, который принимает параметры brand, model, year.
# Методы: getBrand(), getModel(), getYear() и getPrice().
# setPrice(double price).
# Метод printCarInfo(), который выводит:
# Бренд: <brand>, Модель: <model>, Год: <year>, Цена: <price>
# В методе main создайте объект класса Car, задайте цену через сеттер, а затем выведите всю информацию о машине.

# class Car():
#     def __init__(self, brand=None, model=None, year=None, price=0):
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self._price = price

#     @classmethod
#     def create_car_brand_model_year(cls, brand, model, year, price=0):
#         return  cls(brand = brand, model = model, year = year, price = price)

#     def getBrand(self):
#             return self.brand

#     def getModel(self):
#             return self.model

#     def getYear(self):
#             return self.year  

#     def getPrice(self):
#             return self._price

#     def setPrice(self, price):
#         if price <=0:
#             raise(ValueError('Невозможно установить цену к этой машине'))
#         self._price = price
    
#     def printCarInfo(self):
#         print(f' {self.brand}, Модель: {self.model}, Год: {self.year}, Цена: {self._price}')
# try:
#     car1 = Car("audi", "TT", 2005,)
#     car1.printCarInfo()
#     car1.year = 3000
#     car1.model = 'X6'
#     car1.brand = 'BMW'
#     car1.setPrice(5000)
#     car1.printCarInfo()
# except ValueError as e:
#     print(e)




# Задача 4. Класс "Товар"
# Создайте класс Product с полями:
# name (название товара, тип String),
# category (категория товара, тип String),
# quantity (количество, тип int),
# pricePerUnit (цена за единицу, тип double).
# Реализуйте:
# Конструктор с параметрами для всех полей.
# Геттеры и сеттеры.
# Метод calculateTotalPrice(), который возвращает общую стоимость товара (quantity * pricePerUnit).
# Метод printProductInfo(), который выводит:
# Товар: <name>, Категория: <category>, Количество: <quantity>, Общая стоимость: <totalPrice>
# В методе main создайте объект, измените количество через сеттер, а затем выведите полную информацию о товаре.

# class Product():
#     def __init__(self, name: str, category: str, quantity: int, pricePerUnit: int):
#         self.name = name
#         self.category = category
#         self.quantity = quantity
#         self._pricePerUnit = pricePerUnit
    
#     def calculateTotalPrice(self):
#         return (self.quantity * self._pricePerUnit)


    # def printProductInfo(self):
#             return print(f'Товар: {cls.name}, Категория: {cls.category}, Количество: {cls.quantity}, Общая стоимость: {cls._pricePerUnit}')

# try:
#     cheese = Product('сыр', 'молочные товары', 8, 30)
#     cheese.calculateTotalPrice()
#     cheese.printProductInfo()
# except ValueError as e:
#     print(e)


# Задача 5. Класс "Студент"
# Создайте класс Student с полями:
# name (имя, тип String),
# studentId (идентификатор студента, тип int),
# gpa (средний балл, тип double).
# Реализуйте:
# Конструктор для всех полей.
# Геттеры и сеттеры.
# Метод printStudentDetails(), который выводит:
# Студент: <name>, ID: <studentId>, GPA: <gpa>
# В методе main создайте массив из объектов Student, заполните его, и выведите данные каждого студента.

# class Student():
#     def __init__(self, name:str, studentId:int, gpa:float):

#         if studentId <0 :
#             raise ValueError("ID должен быть положительным числом")
        
#         if gpa <0 or gpa > 5.0:
#             raise ValueError("GPA не может быть меньше 0")

#         self.name = name
#         self.studentId = studentId
#         self.gpa = gpa

    
#     def printStudentDetails(self):
#         return print(f'Студент {self.name}, ID:{self.studentId}, GPA:{self.gpa}')


# try:
#     student_list = []
#     Petr = Student('Петр', 1, 4.2)
#     Sasha = Student('Саша', 2, 5)
#     Vasya = Student('Вася', 3, 4.3)
#     Masha = Student('Маша', 4, 3.5)
#     student_list.append(Petr)
#     student_list.append(Sasha)
#     student_list.append(Vasya)
#     student_list.append(Masha)
#     for person in student_list:
#         person.printStudentDetails()

# except ValueError as e:
#     print(e)

# Задача 7. Класс "Курс Валют"
# Создайте класс Currency с полями:
# name (название валюты, тип String),
# rateToUSD (курс валюты к доллару США, тип double).
# Реализуйте:
# Конструктор для инициализации полей.
# Геттеры и сеттеры.
# Метод convertToUSD(double amount), который возвращает сумму в долларах для заданного количества валюты.
# Метод printCurrencyInfo(), который выводит:
# Валюта: <name>, Курс к USD: <rateToUSD>
# В методе main создайте объект валюты, выведите курс и выполните конвертацию заданной суммы в USD.


# class Currency():
#     def __init__(self, name, rateToUsd):
#         self.name = name
#         self.rate_to_usd = rateToUsd
    
#     def convertToUSD(self, value):  
#         return float(value / self.rate_to_usd)

#     def printCurrencyInfo(self):
#         return print(f'Валюта: {self.name}, Курс к USD: {self.rate_to_usd}')

# try:
#     rub = Currency("Рубль", 100)
#     euro = Currency('Евро', 1.2)
#     usd = Currency("Доллар", 1)

#     rub.printCurrencyInfo()
#     euro.printCurrencyInfo()
#     usd.printCurrencyInfo()
    
#     print(rub.convertToUSD(200))
#     print(euro.convertToUSD(3))
#     print(usd.convertToUSD(3))

# except ValueError as e:
#     print(e)


# Задача 8. Класс "Телефон"
# Создайте класс Phone с полями:
# brand (бренд телефона, тип String),
# model (модель телефона, тип String),
# price (цена телефона, тип double).
# Реализуйте:
# Конструктор для всех полей.
# Геттеры и сеттеры.
# Метод applyDiscount(double percentage), который уменьшает цену на заданный процент.
# Метод printPhoneDetails(), который выводит:
# Телефон: <brand> <model>, Цена: <price>


# В методе main создайте телефон, примените скидку и выведите его характеристики.

# Задача 9. Класс "Сотрудник"
# Создайте класс Employee с полями:
# name (имя сотрудника, тип String),
# position (должность, тип String),
# salary (зарплата, тип double).
# Реализуйте:
# Конструктор для всех полей.
# Геттеры и сеттеры.
# Метод increaseSalary(double percentage), который увеличивает зарплату на заданный процент.
# Метод printEmployeeInfo(), который выводит:
# Сотрудник: <name>, Должность: <position>, Зарплата: <salary>


# В методе main создайте нескольких сотрудников, увеличьте их зарплату и выведите их данные.

# Задача 10. Класс "Треугольник"
# Создайте класс Triangle с полями:
# a (сторона A, тип double),
# b (сторона B, тип double),
# c (сторона C, тип double).
# Реализуйте:
# Конструктор для всех сторон.
# Геттеры и сеттеры.
# Метод calculatePerimeter(), который возвращает периметр треугольника.
# Метод calculateArea(), который возвращает площадь треугольника по формуле Герона.
# Метод printTriangleInfo(), который выводит стороны, периметр и площадь.
# В методе main создайте объект треугольника и выведите его данные.

# Задача 11. Класс "Игрок"
# Создайте класс Player с полями:
# nickname (никнейм, тип String),
# level (уровень, тип int),
# score (очки, тип int).
# Реализуйте:
# Конструктор с параметрами для всех полей.
# Геттеры и сеттеры.
# Метод levelUp(), который увеличивает уровень на 1.
# Метод addScore(int points), который добавляет очки.
# Метод printPlayerInfo(), который выводит:
# Игрок: <nickname>, Уровень: <level>, Очки: <score>


# В методе main создайте игрока, поднимите уровень, добавьте очки и выведите данные.

# Задача 12. Класс "Прямоугольник"
# Создайте класс Rectangle с полями:
# width (ширина, тип double),
# height (высота, тип double).
# Реализуйте:
# Конструктор с параметрами для всех полей.
# Геттеры и сеттеры.
# Методы:
# calculateArea(), возвращает площадь прямоугольника.
# calculatePerimeter(), возвращает периметр.
# Метод printRectangleInfo(), который выводит:
# Прямоугольник: Ширина = <width>, Высота = <height>, Площадь = <area>, Периметр = <perimeter>


# В методе main создайте объект, выведите его площадь и периметр.

# Задача 13. Класс "Клиент Интернет-магазина"
# Создайте класс Customer с полями:
# name (имя клиента, тип String),
# email (почта, тип String),
# purchaseHistory (история покупок, тип List<String>).
# Реализуйте:
# Конструктор для имени и почты.
# Методы:
# addPurchase(String item), добавляет товар в историю покупок.
# printPurchaseHistory(), выводит:
# Клиент: <name>, История покупок: <history>


# В методе main создайте клиента, добавьте несколько покупок и выведите историю.

# Задача 14. Класс "Компания"
# Создайте класс Company с полями:
# name (название компании, тип String),
# employees (количество сотрудников, тип int),
# revenue (доход, тип double).
# Реализуйте:
# Конструктор для всех полей.
# Геттеры и сеттеры.
# Метод printCompanyInfo(), который выводит:
# Компания: <name>, Сотрудников: <employees>, Доход: <revenue>


# В методе main создайте объект компании и выведите его данные.

# Задача 15. Класс "Круг"
# Создайте класс Circle с полями:
# radius (радиус, тип double).
# Реализуйте:
# Конструктор с параметром radius.
# Методы:
# calculateCircumference(), возвращает длину окружности.
# calculateArea(), возвращает площадь круга.
# Метод printCircleInfo(), который выводит:
# Круг: Радиус = <radius>, Площадь = <area>, Длина окружности = <circumference>


# В методе main создайте круг и выведите его данные.