#Farmacia
def farmacia(telefone, nome, endereco, cnpj):
    print('-----------Farmacia----------')
    print(f'Nº telefone: {telefone}')
    print(f'Nome: {nome}')
    print(f'Nº de endereço: {endereco}')
    print(f'Nº CNPJ: {cnpj}')

telefone = input('Nº Telefone: ')
nome = input('Nome da farmacia: ')
endereco  = input('Nº Endereço: ')
cnpj = input('Número do CNPJ: ')

#Produto
def produto(codigo, qtd, valor):
    print('')
    print('-----------Produto-----------')
    print(f'Codigo: {codigo}')
    print(f'Quantidade: {qtd}')
    print(f'Valor: {valor}')

codigo = input('Codigo: ')
qtd = int(input('Quatidade: '))
valor  = float(input('Valor do prduto: '))

#Farmaceutico
def farmaceutico(rg, nome):
    print('')
    print('---------Farmaceutico--------')
    print(f'Numero do RG: {rg}')
    print(f'Nome do farmaceutico: {nome}')

rg = input('RG do farmaceutico: ')
nome  = input('Nome do formaceutico: ')

print('')
print('FICHA TECNICA')
farmacia(telefone, nome, endereco, cnpj)
farmaceutico(rg, nome)
produto(codigo, qtd, valor)
