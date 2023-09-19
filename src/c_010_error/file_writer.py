filename = 'file/programming.txt'

with open(filename, 'w') as file_object:
    file_object.write('i love programming.\n')
    
with open(filename, 'a') as file_object:
    file_object.write('i love video game.\n')
    file_object.write('i love music.\n')