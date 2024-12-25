class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return f"Year: {self.year} Make: {self.make} Model: {self.model}"

car = Car("Hyundai", "i40", 2013)
print(car.get_info())
