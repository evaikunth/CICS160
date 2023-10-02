import Car

class GasolineCar(Car.Car):
    def __init__(self, make_model = "None assigned", num_doors = 4, max_passengers = 5, gas_tank_size = -1):
        super().__init__(make_model, num_doors, max_passengers)
        self.gas_tank_size = gas_tank_size

    def get_gas_tank_size(self):
        return self.gas_tank_size

    def set_gas_tank_size(self, size):
        self.gas_tank_size = size

if __name__ == "__main__":
    g1 = GasolineCar()
    g1.set_gas_tank_size(40)
    print(g1.get_gas_tank_size())
