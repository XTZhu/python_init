# -*- coding: UTF-8 -*-

class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Dog类的构造函数被调用了.')
        print(f'{self.name} is a {self.age} years old dog.')

    def sit(self, sound=""):
        print(self.name.title() + " 坐下了.")

    def roll_over(self):
        leading = str(self.age) + '岁的' + self.name.title()
        if self.age < 10:
            print(leading + " 翻了个跟头.")
        else:
            print(leading + " 打了个滚.")


andy = Dog('andy', 5)
andy.name
andy.age
# andy.sit('wof')
# andy.roll_over()

jim = Dog('jim',12)
jim.sit()
jim.roll_over()
