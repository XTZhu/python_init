import json

numbers = [2, 1, 4, 5, 6, 6]

filename = 'file/numbers.json'

with open(filename, 'w') as file_object:
    json.dump(numbers, file_object)
