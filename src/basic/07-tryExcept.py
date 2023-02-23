# Try/Except
salary = input('Enter your salary: ')
bonus = input('Enter your bonus: ')

try:
    increase = (float(salary) * float(bonus)) / 100
    print(f'Increase: {increase}')
    total = float(salary) + float(increase)
    print(f'Total: {total}')
except:
    print('Invalid data, try again...')

