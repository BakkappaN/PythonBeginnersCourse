# Import another python file & class
from Chapter05.classes_objects_01 import Car

# Object 1 creation
object1 = Car()
print('Model : ', object1.model) # access variables
print('Color : ', object1.color)
print('Price : ', object1.price)
object1.startCar() # invoke method