N = int(input("insira a quantidade de números reais: "))
somaReais = 0

nAtual = 0
while nAtual < N:
  entrada = float(input(f"insira o {nAtual + 1}º número real da soma: "))
  if entrada >= 0:
    somaReais += entrada
  nAtual += 1

print(f'soma dos valores positivos: {somaReais}')