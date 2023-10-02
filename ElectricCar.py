import Car
class ElectricCar(Car.Car):
    def __init__(self, make_model = "None assigned", num_doors = 4, max_passengers = 5):
        super().__init__(make_model, num_doors, max_passengers)
        

    def __str__(self) -> str:
        return super().__str__() + "\nELECTRIC CAR"

if __name__ == "__main__":
    e1 = ElectricCar()
    print(e1)
