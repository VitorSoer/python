name = input('Enter your name: ')
height = input('Enter your height: ')
weight = input('Enter your weight: ')

imc = float(weight) / (float(height) ** 2)
result = f'Name: {name} | IMC: {imc:.2f}'

print(result)
