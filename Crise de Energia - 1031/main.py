numeroRegioes = int(input())
salto = int(input())
listaRegioes = []
listaApagados = []
indice = 0
if numeroRegioes >= 13 and numeroRegioes <= 100:
    listaApagados.append(1)
    for i in range(numeroRegioes):
        listaRegioes.append(i+1)
    
    while len(listaRegioes) > 1:
        indice = (indice + salto) % len(listaRegioes)
        apagados = listaRegioes.pop(indice)
        listaApagados.append(apagados)
    print(apagados)
else:
    pass