class Device:
    def __init__(self, height, width, given_name):
        self.height = height
        self.width = width
        self.name = given_name
    
    def power_on(self):
        print("Device is powered on.")

class Computer(Device):
    def power_on(self):
        print("Computer is powered on.")
    
    def power_off(self):
        print("Computer is powered off.")
    
    def beep(self):
        print("Computer is beeping.")

phone = Device(10, 4, "Phone")
phone.power_on()

pc = Computer(20, 30, "Dell")
pc.power_off()