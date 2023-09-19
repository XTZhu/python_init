"""一个可用于表示汽车的类"""

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0  # 里程表

    def get_descriptive_name(self):
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()

    def read_odometer(self):
        print(f'This car has {self.odometer} miles on it.')

    def update_odometer(self, mileage):
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print('You can not roll back an odometer!')

    def increment_odometer(self, miles):
        self.odometer += miles

    def fill_gas_tank(self):
        print('油箱已经灌满了')
