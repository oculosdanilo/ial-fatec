tempo = int(input())

segundos = 0
minutos = 0
horas = 0

while tempo != 0:

  if tempo >= 3600:
    tempo -= 3600
    horas += 1

  elif tempo >= 60:
    tempo -= 60
    minutos += 1

  else:
    segundos = tempo
    tempo = 0

print(f'{horas}:{minutos}:{segundos}')
