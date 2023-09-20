aliens = []

for alien in range(0, 30):
    new_alien = {}
    if (alien < 3):
        new_alien = {'color': 'green', 'points': 6, 'speed': 'slow'}
    elif alien < 6:
        new_alien = {'color': 'yellow', 'points': 8, 'speed': 'medium'}
    else:
        new_alien = {'color': 'red', 'points': 10, 'speed': 'fast'}
    aliens.append(new_alien)

for alien in aliens[:8]:
    print(alien)
