class Car:
    def __init__(self, mark, model, year):
        self.mark = mark
        self.model = model
        self.year = year

    def getinfo (self):
        return f"{self.year} {self.mark} {self.model}"

My_car = Car("Audi", "A4", 2021)
print(My_car.getinfo())
print("hfg")