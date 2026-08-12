#Create Parent class Vehicle and child classes Car Brake and Truck
#should have common propertities like brand, Speed, fuel
#Child should have one Unique Property

class Vehicle:
    def __init__(self,brand,speed,fuel):
        self.brand = brand
        self.speed = speed
        self.fuel = fuel
class Car(Vehicle):
    def __init__(self,brand,speed,fuel,Numberofdoors):
        super().__init__(brand,speed,fuel)
        self.Numberofdoors = Numberofdoors
    def display_car(self):
        print("Brand: ",self.brand)
        print("Speed: ",self.speed)
        print("Fuel: ",self.fuel)
        print("Numnber of doors: ",self.Numberofdoors)
class Bike(Vehicle):
    def __init__(self,brand,speed,fuel,CC):
        super().__init__(brand,speed,fuel)
        self.CC= CC
    def display_bike(self):
        print("Brand: ",self.brand)
        print("Speed: ",self.speed)
        print("Fuel: ",self.fuel)
        print("CC: ",self.CC)
class Truck(Vehicle):
    def __init__(self,brand,speed,fuel,loadcapacity_):
        super().__init__(brand,speed,fuel)
        self.loadcapacity = loadcapacity
    def display_truck(self):
        print("Brand: ",self.brand)
        print("Speed: ",self.speed)
        print("Fuel: ",self.fuel)
        print("Load capacity: ",self.loadcapacity) 

c_brand = input("Enter the Brand of the Car: ")
b_brand = input("Enter the Brand of the Bike: ")
t_brand = input("Enter the Brand of the Truck: ")
c_speed = int(input("Enter the Speed of the Car: "))
b_speed = int(input("Enter the Speed of the Bike: "))
t_speed = int(input("Enter the Speed of the Truck: "))
c_fuel = input("Enter the Fuel of the Car: ")
b_fuel = input("Enter the Fuel of the Bike: ")
t_fuel = input("Enter the Fuel of the Truck: ")
c_numberofdoors = int(input("Enter the Number of Doors of the Car: "))
b_cc = int(input("Enter the CC of the Bike: "))
t_loadcapacity = int(input("Enter the Load Capacity of the Truck: "))
C=Car(c_brand,c_speed,c_fuel,c_numberofdoors)
B=Bike(b_brand,b_speed,b_fuel,b_cc)
T=Truck(t_brand,t_speed,t_fuel,t_loadcapacity)
C.display_car()
B.display_bike()
T.display_Truck()


