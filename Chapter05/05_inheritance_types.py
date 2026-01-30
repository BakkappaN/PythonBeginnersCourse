print("Multi-level Inheritance") 
class A: 
    def funtion1(self): 
        print('Running function1...') 

class B(A): # Multi-level Inheritance
    def funtion2(self): 
        print('Running function2...') 

class C(B): # Multi-level Inheritance
    def funtion3(self): 
        print('Running function3...') 

object1 = C() 
object1.funtion1() 
object1.funtion2() 
object1.funtion3() 

print("Multiple Inheritance") 
class A: 
    def function1(self): 
        print('Running function1...') 

class B: 
    def function2(self): 
        print('Running function2...') 

class C(A, B):   # multiple inheritance 
    def function3(self): 
        print('Running function3...') 

object1 = C() 
object1.function1() 
object1.function2() 
object1.function3() 

print("Hierarchical Inheritance") 
class A: 
    def function1(self): 
        print('Running function1...') 

class B(A):  # Hierarchical Inheritance 
    def function2(self): 
        print('Running function2...') 

class C(A): # Hierarchical Inheritance 
    def function3(self): 
        print('Running function3...') 

obj_b = B() 
obj_c = C() 
obj_b.function1() 
obj_b.function2() 

obj_c.function1() 
obj_c.function3() 