# Задание 1
import random

class MusicAlbum:
    def __init__(self, title, artist, release_year, genre, tracklist):
        self.title = title
        self.artist = artist
        self.release_year = release_year
        self.genre = genre
        self.tracklist = tracklist

    def play_random_track(self):
        random_track = random.choice(self.tracklist)
        print("Playing random track:", random_track)

# Пример использования
album = MusicAlbum("Album Title", "Artist Name", 2023, "Pop", ["Track 1", "Track 2", "Track 3"])
album.play_random_track()

# Задание 2
class Student:
    def __init__(self, name, age, grade, scores):
        self.name = name
        self.age = age
        self.grade = grade
        self.scores = scores

    def average_score(self):
        return sum(self.scores) / len(self.scores)

# Задание 3
class Recipe:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def print_ingredients(self):
        print("Ingredients for", self.name + ":")
        for ingredient in self.ingredients:
            print(ingredient)

    def cook(self):
        print("Cooking", self.name)

# Задание 4
class Publisher:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def get_info(self):
        print("Publisher:", self.name)
        print("Location:", self.location)

    def publish(self, message):
        print("Publishing:", message)

class BookPublisher(Publisher):
    def __init__(self, name, location, num_authors):
        super().__init__(name, location)
        self.num_authors = num_authors

class NewspaperPublisher(Publisher):
    def __init__(self, name, location, num_pages):
        super().__init__(name, location)
        self.num_pages = num_pages

# Задание 5
class BankAccount:
    def __init__(self):
        self.__balance = 0
        self.__interest_rate = 0
        self.__transactions = []

    def deposit(self, amount):
        self.__balance += amount
        self.__transactions.append(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            self.__transactions.append(f"Withdrew: {amount}")
        else:
            print("Insufficient balance.")

    def add_interest(self):
        interest = self.__balance * self.__interest_rate
        self.__balance += interest
        self.__transactions.append(f"Interest added: {interest}")

    def history(self):
        for transaction in self.__transactions:
            print(transaction)

# Задание 6
class Employee:
    def __init__(self, name, age, salary, bonus):
        self.__name = name
        self.__age = age
        self.__salary = salary
        self.__bonus = bonus

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_salary(self):
        return self.__salary

    def set_bonus(self, bonus):
        self.__bonus = bonus

    def get_bonus(self):
        return self.__bonus

    def get_total_salary(self):
        return self.__salary + self.__bonus

# Задание 7
class Animal:
    def __init__(self, name, species, legs):
        self.name = name
        self.species = species
        self.legs = legs

    def voice(self):
        print(f"{self.name} makes a sound.")

    def move(self):
        print(f"{self.name} is moving.")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog", 4)
        self.breed = breed

    def bark(self):
        print(f"{self.name} barks.")

class Bird(Animal):
    def __init__(self, name, wingspan):
        super().__init__(name, "Bird", 2)
        self.wingspan = wingspan

    def fly(self):
        print(f"{self.name} flies.")

# Задание 8
class Shape:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def describe(self):
        print(f"Shape: {self.name}, Color: {self.color}")

class Circle(Shape):
    def __init__(self, name, color, radius):
        super().__init__(name, color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, name, color, length, width):
        super().__init__(name, color)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, name, color, base, height):
        super().__init__(name, color)
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Задание 9
class Candy:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

class Chocolate(Candy):
    def __init__(self, name, price, weight, cocoa_percentage, chocolate_type):
        super().__init__(name, price, weight)
        self.cocoa_percentage = cocoa_percentage
        self.chocolate_type = chocolate_type

class Gummy(Candy):
    def __init__(self, name, price, weight, flavor, shape):
        super().__init__(name, price, weight)
        self.flavor = flavor
        self.shape = shape

class HardCandy(Candy):
    def __init__(self, name, price, weight, flavor, filled):
        super().__init__(name, price, weight)
        self.flavor = flavor
        self.filled = filled

# Задание 10
def info_decorator(func):
    def wrapper(self):
        print("Name:", self.name)
        print("Rank:", self._rank)
        print("Service Number:", self._service_number)
        func(self)
    return wrapper

class Soldier:
    def __init__(self, name, rank, service_number):
        self.name = name
        self._rank = rank
        self._service_number = service_number

    @info_decorator
    def get_rank(self):
        pass

    def confirm_service_number(self, number):
        return number == self._service_number

    def promote(self):
        pass

    def demote(self):
        pass
