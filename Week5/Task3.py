# Create a program to demonstrate the concept of
#  inheritance by creating a base class for a vehicle and derived
#  classes for car and bike

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"Vehicle Make: {self.make}, Model: {self.model}")

class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()
        print(f"Number of Doors: {self.num_doors}")

class Bike(Vehicle):
    def __init__(self, make, model, has_basket):
        super().__init__(make, model)
        self.has_basket = has_basket

    def display_info(self):
        super().display_info()
        print(f"Has Basket: {self.has_basket}")

if __name__ == "__main__":
    car = Car("Toyota", "Camry", 4)
    bike = Bike("Giant", "Escape 3", True)

    print("Car Information:")
    car.display_info()

    print("\nBike Information:")
    bike.display_info()