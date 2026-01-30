# Duck Typing 
class Animal:
    def speak(self):
        print('Animal makes sound')

class Dog:
    def speak(self):
        print('Dog barks')

class Cat:
    def speak(self):
        print('Cat meows')

def make_sound(animal):
    animal.speak() # polymorphism

make_sound(Animal())
make_sound(Dog())
make_sound(Cat())