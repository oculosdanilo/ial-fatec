NEG = []
nNEG = 0
POS = []
nPOS = 0
A = []

N = int(input("insira um número inteiro entre 0 e 50: "))

while N > 50 or N < 0:
  print("número inválido!\n")
  N = int(input("insira um número inteiro entre 0 e 50: "))

cont = 0
while cont < N:
  A.append(float(input(f"insira o {cont + 1}º número real da lista: ")))

  cont += 1

for nReal in A:
  if nReal < 0:
    NEG.append(nReal)
    nNEG += 1
  else:
    POS.append(nReal)
    nPOS += 1

print(f'{nNEG} valor(es) negativo(s): {NEG}')
print(f'{nPOS} valor(es) positivo(s): {POS}')
