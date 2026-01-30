# Polymorphism
class Animal:
    def speak(self): 
        print('Animal makes sound')

class Dog(Animal):
    def speak(self): # method overriding
        print('Dog barks')

class Cat(Animal):
    def speak(self): # method overriding
        print('Cat meows')

animals = [Animal(), Dog(), Cat()]

for obj in animals:
    obj.speak() # polymorphism