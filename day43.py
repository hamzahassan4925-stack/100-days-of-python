class Car:
    @staticmethod
    def start():
        print("car is starting...")


    @staticmethod
    def stop():
        print("car is sti=oping...") 


class Toyota(Car):
    def __init__(self, name):
        self.name = name

car1 = Toyota("Toyota Camry")
car2 = Toyota("Toyota Corolla")
car3 = Toyota("Toyota RAV4")

print(car1.start())
print(car2.stop())
print(car3.start())