resultadoTrilhas = []

for i in range(int(input())):
    inputTrilhas = list(map(int, input().split()))
    trilhas = inputTrilhas[1:inputTrilhas[0]+1]
    subidas = 0
    subidasReverse = 0

    tamanho = len(trilhas)

    for j in range(tamanho - 1):
        if trilhas[j+1] > trilhas[j]:
            subidas += trilhas[j+1] - trilhas[j]

    trilhas.reverse()
    for j in range(tamanho - 1):
        if trilhas[j+1] > trilhas[j]:
            subidasReverse += trilhas[j+1] - trilhas[j]

    menorEsforco = subidas if subidas < subidasReverse else subidasReverse
    resultadoTrilhas.append((i+1, menorEsforco))

melhorIndice, melhorEsforco = resultadoTrilhas[0]

for indice, esforco in resultadoTrilhas[1:]:
    if esforco < melhorEsforco or (esforco == melhorEsforco and indice < melhorIndice):
        melhorIndice, melhorEsforco = indice, esforco

print(melhorIndice)
