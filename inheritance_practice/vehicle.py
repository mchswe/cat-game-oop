class Vehicle:
    def __init__(self, given_name, speed, size):
        self.name = given_name
        self.speed = speed
        self.size = size
    
    def switch_on(self):
        print("Vehicle is switched on.")
    
    def drive(self):
        print("Vehicle is driving.")

    def fix(self):
        print("Vehicle is being fixed.")
    
class Car(Vehicle):
    def switch_on(self):
        print("Car is switched on.")
    
    def drive(self):
        print("Car is driving.")
    
    def fix(self):
        print("Car is being fixed.")
    
    def drift(self):
        print("Car is drifting.")

class Motorbike(Vehicle):
    def switch_on(self):
        print("Bike is switched on.")
    
    def drive(self):
        print("Bike is driving.")
    
    def fix(self):
        print("Bike isbeing fixed.")
    
    def wheelie(self):
        print("Bike is being wheelied.")

truck = Vehicle("Scania", 42, 1000)
supra = Car("Supra", 90, 450)
ducati = Motorbike("Ducati", 115, 90)
