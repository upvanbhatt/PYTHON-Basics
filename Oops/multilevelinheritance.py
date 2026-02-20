#one base class and more than one derived class


class Car:
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped.")

class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand

class Fortunar(ToyotaCar):
    def __init__(self, type):
        self.type =type


car1 = Fortunar ("diesel")
car1.start()

