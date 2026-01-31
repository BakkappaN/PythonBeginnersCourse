# Import ABC & abstractmethod
from abc import ABC, abstractmethod 
class Animal(ABC): 
    def function1(self): # normal method 
        print("Function1 is running") 

    @abstractmethod # abstract method 
    def sound(self): 
        pass 

class Dog(Animal): 
    def sound(self): #override method 
        print("Dog barks") 

class Cat(Animal): 
    def sound(self): #override method 
        print("Cat meows") 

animals = [Dog(), Cat()] 
for animal in animals: 
    animal.sound() 

# Invoke inherited method 
obj1 = Dog() 
obj1.function1() 

# Invoke inherited method 
obj2 = Cat() 
obj2.function1() 