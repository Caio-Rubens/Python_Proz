faturamento = 1200
custo = 750

novas_vendas = 100
faturamento = faturamento + novas_vendas

imposto =  faturamento * 0.1
lucro = faturamento - custo - imposto

margem_lucro = lucro / faturamento

print('Faturamento foi de', faturamento)
print('O custo foi de', custo)
print('O lucro foi de', lucro)
print('A margem de lucro foi de', round(margem_lucro, 3))

mensagem = 'O faturamento da loja foi de tanto'
email = 'emailqualquer@gmail.com'

teve_lucro = True

tempo_contrato = 170

tempo_anos = 170 / 12
print('Tempo em anos', int(tempo_anos))

tempo_meses = 170 % 12
print('Tempo em anos', int(tempo_meses))