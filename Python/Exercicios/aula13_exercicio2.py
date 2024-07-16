dic_item = {'pera':1.45, 'laranja':3.5, 'abacaxi':8.48, 'mexirica':5.78}


nome_item = input('Nome produto: ')
preco_item = input('Valor do produto: ')

if nome_item in dic_item:
    dic_item[nome_item] = preco_item
    print(dic_item)

else:
    dic_item[nome_item] = preco_item
    print(dic_item)