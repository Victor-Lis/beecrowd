tipo = input()
respostas = [resposta for resposta in input().split() if resposta == tipo]
print(len(respostas))