dinheiro = int(input())
dinheiroSobrando = dinheiro

cem = 0
cinquenta = 0
vinte = 0
dez = 0
cinco = 0
dois = 0
um = 0

while dinheiroSobrando != 0:

  if dinheiroSobrando >= 100:
    dinheiroSobrando -= 100
    cem += 1

  elif dinheiroSobrando >= 50:
    dinheiroSobrando -= 50
    cinquenta += 1

  elif dinheiroSobrando >= 20:
    dinheiroSobrando -= 20
    vinte += 1

  elif dinheiroSobrando >= 10:
    dinheiroSobrando -= 10
    dez += 1

  elif dinheiroSobrando >= 5:
    dinheiroSobrando -= 5
    cinco += 1

  elif dinheiroSobrando >= 2:
    dinheiroSobrando -= 2
    dois += 1

  else:
    dinheiroSobrando -= 1
    um += 1

print(dinheiro)
print(
  f'{cem} nota(s) de R$ 100,00\n{cinquenta} nota(s) de R$ 50,00\n{vinte} nota(s) de R$ 20,00\n{dez} nota(s) de R$ 10,00\n{cinco} nota(s) de R$ 5,00\n{dois} nota(s) de R$ 2,00\n{um} nota(s) de R$ 1,00')
