class Vehcile: #Redudancy Kam krta, RObust code, Error prone
    def __init__(self,color,radius_tire = "10cm",headlight=2) -> None:
        self.radius_tire = radius_tire
        self.color = color
        self.headlight = headlight
    
    def move(self):
        #x = X+10,X = X-10
        print("BIKE IS MOVING")
        pass

class Bike(Vehcile):
    def __init__(self,color):
        super().__init__(color)
        self.no_of_tire = 2
        print("BIKE IS CREATED")

class Car(Vehcile):
    def __init__(self,color) -> None:  # Dunder 
        super().__init__(color)
        print("CAR IS CREATED")

# car = Car()
# print(car.move())
bike = Bike("Blue")
print(bike.color)
print(bike.radius_tire)
car = Car("YELLOW")
print(car.color)