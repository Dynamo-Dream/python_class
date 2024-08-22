class Car: # Default Arguments
    def __init__(self, colour = "Red", no_of_tire = 4, radius_tire = "5cm", password = "1234556") -> None: #Constructor
        self.colour = colour
        self.no_of_tire = no_of_tire
        self.radius_tire = radius_tire
        self.__password = password
        self._email = "ASDASDS.@mail.com" #Protected Attriutes => JAVA or C++ or C# OOPS Language
        #SHow peice _eamil, Class andar access bahar access batane mt krna
    def login(self):
        self.__password
        pass
         #Private Attributes

    @staticmethod #decorator function ke andar function
    def hello():
        print("Hi Player I am Red Small Car")

    def move_left(self):
        pass
        #x = x+10
    def move_right(self):
        pass
        #x = x-10  

    def move(self,key_press = "Left"):
        if key_press == "Left":
            print("LEFT BUTTON")
            self.move_left()

        elif key_press == "Right":
            print("RIGHT BUTTON")
            self.move_right()

small_car = Car()
print(small_car._email)
#print(small_car.__password)
print(small_car.login())
# print(small_car.hello())
small_car.radius_tire = 10
print(small_car.radius_tire)
# print(small_car.colour)
# for i in range(10):
#     if i%2 == 0: #even number
#         small_car.move("Left")
#     else:
#         small_car.move("Right")

print("RUNNNING MONSTETER TRUCK ------------------------------------------------")

# monster_truck = Car()
# print(monster_truck.colour)
# for i in range(10):
#     if i%2 == 0: #even number
#         monster_truck.move("Left")
#     else:
#         monster_truck.move("Right")



# small_car is an instance of Class Car #Object
# monster_truck = Car()
# monster_truck.radius_tire = "15cm"
# monster_truck.colour = "Blue"


# print(small_car.colour)
# print(monster_truck.colour)



