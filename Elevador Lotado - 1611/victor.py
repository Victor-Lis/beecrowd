
casos = int(input())

for _ in range(casos):
    ultimoAndar, porVez, pessoas = map(int, input().split())
    andares = list(map(int, input().split()))

    andares.sort()

    # print(andares)
    
    maximoEnergia = 0
    while len(andares):
        vez = []
        while len(vez) < porVez and len(andares) > 0:
            vez.append(andares.pop())
        # print(vez)
        maior = max(vez)
        maximoEnergia += maior * 2
    print(maximoEnergia)