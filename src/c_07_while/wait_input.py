import datetime
import time


def wait_input():
    time.sleep(2)
    print('\n')


message = input("我是山谷，对我说话吧: ")
print(message)
wait_input()

prompt = '开玩笑的, 让我介绍一下我自己'
prompt += '\n我是机器人'
prompt += ' 你叫咩名? \n请输入你的年龄:'

name = input(prompt)
wait_input()

print("hello " + name + " 很开心认识你")
wait_input()
tall_prompt = '你多大了？ 我算一下你的生肖, 请输入你的年龄:'

age = input(tall_prompt)
age = int(age)


def calculate_chinese_zodiac(year):
    zodiacs = ["鼠", "牛", "虎", "兔", "龙", "蛇", "马", "羊", "猴", "鸡", "狗", "猪"]
    start_year = 1924  # 鼠年开始
    zodiac_index = (year - start_year) % 12
    chinese_zodiac = zodiacs[zodiac_index]
    return chinese_zodiac


current_date = datetime.date.today()

year = current_date.year  # 获取当前年份

your_brithYear = year - age

zodiac = calculate_chinese_zodiac(your_brithYear)
print('稍等，马上算好...')
wait_input()
print(f"{your_brithYear}年的生肖是{zodiac}")
