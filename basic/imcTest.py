name = input('Type your name: ')
height = input('Type your height: ')
weight = input('Type your weight: ')

imc = float(weight) / (float(height) ** 2)
result = f'Name: {name} | IMC: {imc:.2f}'

print(result)
