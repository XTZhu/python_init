alien_0 = {'color': 'gray', 'height': 1.0,
           'speed': 'fast', 'name': 'daft punk', }

# print(alien_0['color'])
# print(alien_0['height'])

aliens = {0: alien_0}

aliens[0]['x_position'] = 50
aliens[0]['color'] = 'yellow'

# for key, value in alien_0.items():
#     print(key + " " + str(value))


del aliens[0]['x_position']

# print(aliens)


# print(alien_0.keys())
# print(alien_0.values())

alien_1 = {}
alien_1['color'] = 'red'
alien_1['height'] = 1.2
alien_1['speed'] = 'slow'
alien_1['name'] = 'guns n roses'

aliens[1] = alien_1

# print(aliens)

# for key in sorted(alien_0.keys()):
# print(key.title() + " " + str(alien_0[key]))


aline_3 = {"name": 'daft punk'}
aline_4 = {"name": 'daft punk copy'}
aliens[3] = aline_3
aliens[4] = aline_4

alien_names = []

for alien in aliens.values():
    alien_names.append(alien['name'])

print(alien_names)

for alien_name in set(alien_names):
    print(alien_name)
