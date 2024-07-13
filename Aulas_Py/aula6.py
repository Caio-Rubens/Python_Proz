def olaMundo(Nome, apelido):
    print(f'{Nome} é {apelido}')

Nome = input('Nome:').capitalize()

olaMundo(Nome, 'VIADO')
if Nome == 'Igor':
    print('True')