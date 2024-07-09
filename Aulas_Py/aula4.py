alunos = []

name = ''

while name != 'sair':
    name = input('Aluno: ').lower()
    if name != 'sair':
        alunos.append(name)

    for nomes in alunos:
        print(nomes)

print(alunos)