# Examples
user_hours = input('What time is it? ')

try:
    hour = int(user_hours)

    if hour >= 0 and hour <= 11:
        print('Good morning!')
    elif hour >= 12 and hour <= 17:
        print('Good afternoon!')
    elif hour >= 18 and hour <= 23:
        print('Good evening!')
    else:
        print('Invalid!')
except:
    print('Please, enter a valid time...')

# --------------------------------------------

user_name = input('Type your name: ')
name = len(user_name)

if name <= 1:
    print('Invalid!')
elif name <= 4:
    print('Too short!')
elif name > 6:
    print('Too long!')
else:
    print('Normal...')
