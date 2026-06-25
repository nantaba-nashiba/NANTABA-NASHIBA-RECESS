class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self._model = model
        self.__price = price

car1 = Car("Toyota", "B3", 6000000000)
print(car1.brand)