n = int(input())

i = 0
while i < n:
  notas = input()
  notasLista = notas.split()

  soma = 0
  soma += float(notasLista[0]) * 2
  soma += float(notasLista[1]) * 3
  soma += float(notasLista[2]) * 5
  media = soma / 10

  print(f'{media:.1f}')

  i += 1
