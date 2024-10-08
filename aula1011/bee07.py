x = 1

while x != 2:
  nota = float(input())
  notaAnterior = -1
  media = -1

  while media == -1:
    if 0 <= nota <= 10:
      if notaAnterior == -1:
        notaAnterior = nota
        nota = float(input())
      else:
        media = (nota + notaAnterior) / 2
    else:
      print("nota invalida")
      nota = float(input())

  print(f'media = {media:.2f}')

  print('novo calculo (1-sim 2-nao)')
  x = int(input())
  
  while x != 1 and x != 2:
    print('novo calculo (1-sim 2-nao)')
    x = int(input())