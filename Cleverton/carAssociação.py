class Driver:
    def __init__(self, name):
        self.__name = name
        self.__cars = []

    def addCar(self, car):
        if car not in self.__cars:
            self.__cars.append(car)
        car.setDriver(self)


    def __str__(self):
        c = [e.getName() for e in self.__cars]
        return f"{self.__name} : {c}"

class Car:
    def __init__(self, name):
        self.__name = name
        self.__driver = None

    def getName(self): return self.__name

    def setDriver(self, driver):
        if self.__driver != driver:
            self.__driver = driver
            driver.addCar(self)

    def __str__(self):
        return f"{self.__name} : {self.__driver}"

d = Driver("João Gabriel não me atropele por favor")
c = Car("Celta")
#c.setDriver(d)
d.addCar(c)
print(f"Driver: {d}")
print(f"Car: {c}")