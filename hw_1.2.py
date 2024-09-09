
class Fruits:   
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight
        
    def info(self):
        print( f"Fruit name: {self.name}, Fruit color: {self.color}, Fruit Weight: {self.weight}")
     
of_fruit = Fruits("Арбуз", 'green-red', '3kg')

of_fruit.info()
class Book:   
    def __init__(self, author, title, pages):
        self.title = title
        self.author = author
        self.pages = pages
        
    def info(self):
         print(f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}")
     
    def check_pages(self):
         if self.pages < 100:
            print('Книга является тонкой')
         elif 100 <= self.pages < 300:
            print('Книга является средней величины')
         elif self.pages >= 300:
            print('Книга толстая')
         else:
            print('Ошибка при вводе значения')
          
of_book = Book('Борис Акунин', 'Статский Советник', 1891)

of_book.info()

of_book.check_pages()
""" 
Домашнее Задание №1 

Задание 1:
Создайте класс Fruits c атрибутами - (name, color, weight)
Создайте три объекта класса и с помощью метода выведите информацию о каждом фрукте 

Задание 2:
Создайте класс Book с атрибутами title (название), author (автор) и pages (количество страниц). 
Добавьте метод check_pages, который будет выводить сообщение о том, является ли книга тонкой (менее 100 страниц), средней (100-300 страниц) или толстой (более 300 страниц).
"""