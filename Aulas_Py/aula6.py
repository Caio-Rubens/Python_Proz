def olaMundo(Nome, apelido):
    print(f'{Nome} é {apelido}')

Nome = input('Nome:').capitalize()

olaMundo(Nome, 'Gay')
if Nome == 'Igor':
    print('True')