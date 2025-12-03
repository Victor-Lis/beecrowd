casosTeste = int(input())

andarPessoas = []
pessoas = []
for i in range(casosTeste):
    energia = 0
    total_andares, capacidade, pessoas = map(int, input().split())
    
    andares = [int(valor) for valor in input().split()[:pessoas]]
   
    andares.sort(reverse=True)
    
    for j in range(0, len(andares), capacidade):
        energia += 2 * andares[j]
        
    print(energia)