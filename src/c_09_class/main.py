from car_extends import Car
from electric_car import ElectricCar

my_car = Car('audi', 'a4', 2016)
my_car_name = my_car.get_descriptive_name()
print(my_car_name)
my_car.fill_gas_tank()

my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla_name = my_tesla.get_descriptive_name()
print(my_tesla_name)
my_tesla.fill_gas_tank()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
