quant = int(input("insira a quantidade de números reais: "))

n = 0
maior = 0
menor = 0
while n < quant: # correção: conferir se o usuario inseriu 0
  real = float(input(f"insira o {n + 1}º número real: "))

  if real > maior:
    maior = real

  if real < menor or menor == 0:
    menor = real

  n += 1

print(f'\nnúmero maior: {maior}\nnúmero menor: {menor}')
