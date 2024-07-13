faturamento = 1200
custo = 700

lucro = faturamento - custo

margem_lucro = lucro / faturamento

print(f'Faturamento da empresa: {faturamento}, Custo:  {custo}, Lucro: {lucro}')

email_cliente = 'caio@gmail.com'

# maiúscula 
email_cliente =  email_cliente.upper()
print(email_cliente)

# minúscula
email_cliente = email_cliente.lower()
print(email_cliente)

# @
print(email_cliente.find('@'))

# comprimento da string
print(len(email_cliente))

# printa valor da posção 4
print(email_cliente[4])

# printa o ultimo valor da string
print(email_cliente[-1])

# printa do valor 0 a ate 0 valor -10 (invertido)
print(email_cliente[0:-10])

# troca gmail por hotmail
novo_email = email_cliente.replace('gmail', 'hotmail')
print(novo_email)

# Title (Coloca letra mauiscula no começo das palavras) e Capitalize (Coloca letra maiuscula na primeira palvra)
nome = 'joão lira'

print(nome.title())
print(nome.capitalize())

# pegar servidor do cliente
posicao_arroba = email_cliente.find('@')
servidor = email_cliente[posicao_arroba:]
print(servidor)

# pegar 1º nome
divisao_nomes = nome.find(' ')
primeiro_nome = nome[:divisao_nomes] 
print(primeiro_nome)

# pegar 2º nome
sergundo_nome = nome[divisao_nomes + 1:]
print(sergundo_nome)

# casos especiais = formatações numericas em um texto

margem_lucro = round(margem_lucro, 2)
print(f'Faturamento da empresa: {faturamento:.2f}, Custo: {custo:.2f}, Lucro: {lucro:.2f}, Margem_lucro: {margem_lucro:.0%}')

