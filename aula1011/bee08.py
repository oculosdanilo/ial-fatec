n = int(input())

cont = 1
while cont <= n:
  print(f'{cont} {cont * cont} {cont * cont * cont}')
  print(f'{cont} {(cont * cont) + 1} {(cont * cont * cont) + 1}')

  cont += 1
