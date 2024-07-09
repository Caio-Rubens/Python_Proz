def criaLista(nomeLista, *valores):
    nomeLista = []
    nomeLista.append(valores)

    for valor in nomeLista:
        print(valor)

criaLista('Musicas', 'Paradise', 'Sky Scrappe', 'Djavu')

criaLista('Instrumentos', 'Violão', 'Bateria', 'Xirofone')
