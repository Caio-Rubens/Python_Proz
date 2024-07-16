# dicionario
dic_produtos = {'pera':1.45, 'laranja':3.5, 'abacaxi':8.48, 'mexirica':5.78}

# pegar um elemento
print(dic_produtos['pera'])

# editar um elemento valor
dic_produtos['abacaxi'] = dic_produtos['abacaxi'] * 0.3
print(dic_produtos['abacaxi'])

# quantidade de itens
print(len(dic_produtos))

# remover um item
dic_produtos.pop('mexirica')
print(dic_produtos)

# adicionar um item ao dicionario
dic_produtos['pecego'] = 4.5
print(dic_produtos)

# verificar se um item exite no dicionario 
if 'pera' in dic_produtos:
    print('Existe.')

else:
    print('Não existe.')

# verificar seu um valor exite em um dicionario (incomum de usar)
if 3.50 in dic_produtos.values():
    print('Existe.')

else:
    print('Não existe.')
