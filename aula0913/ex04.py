quant = int(input("insira a quantidade de números reais: "))

n = 0
maior = 0
menor = 0
while n < quant:
  real = float(input(f"insira o {n + 1}º número real: "))

  if real > 0:
    if real > maior:
      maior = real

    if real < menor or menor == 0:
      menor = real
  else:
    print("número inválido! ignorando...")

  n += 1

print(f'\nnúmero maior: {maior}\nnúmero menor: {menor}')
