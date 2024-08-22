class Car:
    colour = "Blue"
    speed = "10"
    weight = "5"

    def __init__(self): 
        print("Car is created")

    def move(self,key = "Right"):   
        if key == "Right":
            #move(right)
            print("Move RIght")

red_car = Car()
red_car.move()

blue_car = Car()
blue_car.move("Left")





# class Character:
#     name = "Violet" #attributes
#     height = "5.9" #OOPS -> START
#     clothes = "Red"

# violet = Character() #Object
# print(violet.name)
# print(violet.height)
# print(violet.clothes)

# jinx = Character() #Object
# jinx.name = "Zombie"
# jinx.clothes = "Brown"
# jinx.height = 5.6
# print(jinx.name)
# print(jinx.clothes)
# print(jinx.height)

# zongly = Character()
# #zongly.name="zongly"
# print(zongly.name,zongly.clothes,zongly.height)


