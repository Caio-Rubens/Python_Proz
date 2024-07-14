# # inputs
# email = input('Escreva seu e-mail: ')
# nome = input('Seu primeiro nome: ')

# print(email, nome)

# print(f'{nome}, verifique seu email: {email} que enviamos um link de confirmação.')

# faturamente = float(input('Escreva seu faturamento: '))
# imposto = faturamente * 0.1

# print(imposto)

# # lista
# vendas = [100, 50, 14, 20, 30, 700]

# # Somas do elemento
# total_vendas = sum(vendas)
# print(total_vendas)

# # max e min 
# print(max(vendas))
# print(min(vendas))

# # pegar posição 
# print(vendas[4])

# lista_produtos = ['iphone', 'ipad', 'airpod', 'macbook']

# produto_procurado = input('Pesquise pelo produto procurado: ')
# produto_procurado = produto_procurado.lower()

# print(produto_procurado in lista_produtos)

# # adicionar um item
# lista_produtos.append('apple watch')
# print(lista_produtos)

# # remover um item
# lista_produtos.remove('apple watch')
# print(lista_produtos)

# lista_produtos.pop(0)
# print(lista_produtos)

# editar um item
precos = [1000, 1500, 3500]
precos[0] = precos[0] * 1.5
print((precos))

# contar quantas vezes aparece o produto na lista
lista_produtos = ['iphone', 'ipad','iphone', 'airpod', 'macbook','iphone']
print(lista_produtos.count('iphone'))

# ordenar lista string
lista_produtos.sort()
print(lista_produtos)   

lista_produtos.sort(reverse=True)
print(lista_produtos)

# ordenar lista números
precos.sort()
print(precos)

precos.sort(reverse=True)
print(precos)