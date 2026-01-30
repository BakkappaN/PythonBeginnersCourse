# Base class
class Animal:
    str1 = 'JavaScript'
    def __init__(self):
        print('Animal class constructor is invoked...')

    def eat(self):
        print('Animal is eating')

# Sub class
class Dog(Animal):
    str1 = 'Python'
    def __init__(self):
        super().__init__() # calling parent class constructor
        print('Dog class constructor is invoked...')

    def eat(self):
        print('Access variable by super : ', super().str1) # calling parent class variables
        super().eat() # calling parent class method
        print('Dog is eating')

    def bark(self):
        print('Dog is barking...')

object1 = Dog()
object1.eat()
object1.bark()
print('Str1 :', object1.str1)
print('Str2 :', object1.str2)