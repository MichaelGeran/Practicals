name = 0
while not name:
    try:
        name = input('Please enter your name: ')
    except ValueError:
        print('Please enter a name.')
print(name)

