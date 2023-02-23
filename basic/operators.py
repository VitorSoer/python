# And
day = 'monday'
game_day = True
holiday = False

if day == 'sunday' and game_day:
    print('Play!!!')
else:
    print('Work!!!')

# Or
if day == 'sunday' or game_day:
    print('Play!!!')
else:
    print('Work!!!')

# Not
if not holiday:
    print('Work, work, woooooork!')

# In
print('ond' in day)