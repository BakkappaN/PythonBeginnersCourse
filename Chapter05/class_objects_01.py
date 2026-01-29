# Class
class Car:
    model = 'A123'
    color = 'red'
    price = 200000

    def startCar(self):
        print('Car is running...')

# Object 1 creation
object1 = Car()
print('Model : ', object1.model) # access variables
print('Color : ', object1.color)
print('Price : ', object1.price)
object1.startCar() # invoke method

print('==========================')

# Object 2 creation
object2 = Car()
print('Model : ', object2.model) # access variables
print('Color : ', object2.color)
print('Price : ', object2.price)
object2.startCar() # invoke method
