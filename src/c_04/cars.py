cars = ['audi', 'bmw', 'subaru', 'toyota']
peoples = []


for car in cars:
    if (car == 'bmw'):
        print(car.upper())
    else:
        print(car.title())


a = 12
b = 10

if (a > 9 and a < 11 or b < 12):
    print('foo')

if 'BMW'.lower() not in cars:
    print('i not have a BMW')
elif 'toyota' in cars:
    print('i have a toyota!')
# else:
    # print('i have a bmw!')


if peoples:
    for car in cars:
        print(car)
else:
    print('no people buy car!')