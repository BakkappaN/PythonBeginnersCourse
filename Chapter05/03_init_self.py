class Car:

    # Constructor & self
    def __init__(self, model, color, price):
        self.model = model
        self.color = color
        self.price = price

    def show_car_details(self):
        print(f"Model : {self.model}, Color : {self.color}, Price : {self.price}")

object1 = Car('A123', 'white', 200000)
object1.show_car_details()