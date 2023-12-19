class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_information(self):
        return f"{self.make} makes the car" + f" The model of the car is {self.model}" + f"Year of the is {self.year}"