def multiply(x,y):
    multiplication = 1
    for i in range(x,y+1):
        multiplication *= i
    print(multiplication)

def add():
    addy = 0
    for i in range(1,11):
        addy += i
    print(addy)

multiply(11,18)
add()