import json

filename = 'file/numbers.json'

with open(filename) as file_object:
    numbers = json.load(file_object)

print(numbers)
