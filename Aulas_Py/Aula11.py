# # condicionais 
# if (input("Seu nome:").lower()) == 'caio':
#     print('Seu nome é bonito')

# else:
#     print('Seu nome é feio.')

# nome = input("Seu nome:").lower()
# if nome == 'caio':
#     print('Seu nome é bonito')

# else:
#     print('Seu nome é feio.')

# 2º senário
salario = float(input('Qual é o seu sálario: '))

if salario >= 1412:
    aumento = salario * 0.5
    salario = salario + aumento

else:
    aumento = salario * 1.5
    salario = salario + aumento

print(f'Salario do viado é {salario:.2f}')