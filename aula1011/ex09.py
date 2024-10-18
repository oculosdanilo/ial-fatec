from random import randint

N = int(input("insira um número inteiro: "))
lista = []

cont = 0
while cont < N:
  lista.append(randint(0, 1000))

  cont += 1

print(f'lista gerada: {lista}')

X = int(input("tente inserir um número contido na lista: "))

achou = False
while not achou:
  for numero in lista:
    if numero == X or achou:
      achou = True

  if not achou:
    print('   número não encontrado, tente novamente')
    X = int(input("tente inserir um número contido na lista: "))

print(f'{X} consta na lista!')
