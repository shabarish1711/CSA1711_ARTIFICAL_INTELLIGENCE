# Vacuum Cleaner Problem

room = ['Dirty', 'Dirty']
position = 0

print("Initial State:", room)

while 'Dirty' in room:

    if room[position] == 'Dirty':
        print("Cleaning Room", position + 1)
        room[position] = 'Clean'

    if position == 0:
        position = 1
    else:
        position = 0

print("Final State:", room)
