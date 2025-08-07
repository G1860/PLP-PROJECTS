# Base class
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

# Derived class: Car
class Car(Vehicle):
    def move(self):
        return "Driving "

# Derived class: Plane
class Plane(Vehicle):
    def move(self):
        return "Flying ️"

# Derived class: Boat
class Boat(Vehicle):
    def move(self):
        return "Sailing "

# Function to demonstrate polymorphism
def vehicle_move(vehicle):
    print(vehicle.move())

# Create objects
my_car = Car()
my_plane = Plane()
my_boat = Boat()

# Test polymorphism
vehicle_move(my_car)
vehicle_move(my_plane)
vehicle_move(my_boat)
