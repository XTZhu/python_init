from car_extends import Car
from battery import Battery

class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        print('电动车不需要油箱')
