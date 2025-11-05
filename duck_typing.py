

class Animal:
    is_alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Car:
    def speak(self):
        print("HONK!")

    is_alive = False

animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.is_alive)