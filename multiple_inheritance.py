
class Animal:

    def __init__(self, name, age = 18):
        self.name = name
        self.age = age

    def eat(self):
        print(f'{self.name} is eating')

    def sleep(self):
        print(f'{self.name} is sleeping')

class Prey(Animal):
    def flee(self):
        print('I am fleeing...')

class Predator(Animal):
    def hunt(self):
        print('I am hunting...')

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass


rabbit = Rabbit('John')
hawk = Hawk('Doe')
fish = Fish('ooga')

rabbit.flee()
hawk.hunt()
fish.hunt()
fish.flee()

fish.sleep()

rabbit.eat()