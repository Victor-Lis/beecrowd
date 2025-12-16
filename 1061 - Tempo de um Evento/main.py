dia1 = int(input().strip().split("Dia")[1])

horas1, minutos1, segundos1 = map(int, input().strip().split(':'))

dia2 = int(input().strip().split("Dia")[1])

horas2, minutos2, segundos2 = map(int, input().strip().split(':'))

segundos = 0
minutos = 0
horas = 0
dias = 0

if (segundos1 > segundos2):
    segundos += 60 - (segundos1 - segundos2)
    minutos += -1    
else:
    segundos += segundos2 - segundos1
    
if (minutos1 > minutos2):
    minutos += 60 - (minutos1 - minutos2)
    horas += -1
else:
    minutos += minutos2 - minutos1

if (horas1 > horas2):
    horas += 24 - (horas1 - horas2)
    dias += -1
else:
    horas += horas2 - horas1


if (dia1 > dia2):
    dias += dia1 - dia2
else:
    dias += dia2 - dia1

print(dias, "dia(s)")
print(horas, "hora(s)")
print(minutos, "minuto(s)")
print(segundos, "segundo(s)")