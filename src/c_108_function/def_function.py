def greet_user():
    print('hello everyone')


greet_user()


def greet_username(username):
    print('hello ' + username)


greet_username('jessica')


def describe_pet(cat, dog):
    print('I have a cat named ' + cat + ' and a dog named ' + dog)


describe_pet(dog='kitty', cat='xiaobai')
describe_pet('jiafei', 'xiaotian')


def describe_pet(pet_name, animal_type='dog'):
    print('I have a ' + animal_type + ' named ' + pet_name)
    return pet_name.title()


cat_name = describe_pet('xiaobai')
cat2_name = describe_pet('miaomiao', 'cat')
print(cat_name)
print(cat2_name)


def build_person(first_name, last_name, age=''):
    person = {"first_name": first_name, 'last_name': last_name}
    if age:
        person['age'] = age
    return person

bruceLee = build_person('bruce', 'lee')
print(bruceLee)
mickeyMouse = build_person('mickey', 'mouse', 12)
print(mickeyMouse)
