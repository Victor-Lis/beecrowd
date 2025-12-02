casosTeste = int(input())

for i in range(casosTeste):
  qtdCarneiros = int(input())
  carneiros = map(int, input().split(" "))
  print(len(set(carneiros)))
