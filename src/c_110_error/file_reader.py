file_absolute_path = 'F:/workspace_py/python-init/file/pi_digits.txt'
file_path = '../file/pi_digits.txt'

try:
    with open(file_path) as file_object:
        contents = file_object.read()
        print(contents.rstrip())

except FileNotFoundError:
    print('no such file or directory: ' + file_path)
else:
    print('read file success')


# with open(file_absolute_path) as file_object:
#     for line in file_object:
#         print(line.rstrip())

# with open(file_absolute_path) as file_object:
#     lines = file_object.readlines()

# for line in lines:
#     print(line.rstrip())


# with open(file_absolute_path) as file_object:
#     lines = file_object.readlines()

# pi_str = ''
# for line in lines:
#     pi_str += line.strip()

# print(pi_str)
# print(len(pi_str))
