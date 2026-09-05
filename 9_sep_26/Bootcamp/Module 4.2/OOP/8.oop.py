class Car():
    @staticmethod
    def start():
        print("Car is starting...")

    @staticmethod
    def stop():
        print("Car is stopping...")


class Toyota(Car):
    def __init__(self, model):
        self.model = model


car = Toyota("Camry")
car.start()