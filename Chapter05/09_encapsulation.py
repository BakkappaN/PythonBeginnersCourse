print("=== public ===")  
class Employee:
    def __init__(self, salary):
        self.salary = salary  # public

emp = Employee(50000)
print(emp.salary)

print("=== protected ===")  
class Employee:  
	def __init__(self, salary):  
		self._salary = salary # protected 

	def show_salary(self): 
   		print(self._salary) 
 
emp = Employee(50000)  
emp.show_salary()  
print(emp._salary) # accessible, but NOT recommended 

print("=== private ===")  
class Employee:
    def __init__(self, salary):
        self.__salary = salary  # private

    def get_salary(self):
        return self.__salary

    def set_salary(self, amount):
        if amount > 0:
            self.__salary = amount

emp = Employee(50000)
print(emp.get_salary())  # allowed

emp.set_salary(60000)
print(emp.get_salary())  # allowed

# print(emp.__salary) # Error 