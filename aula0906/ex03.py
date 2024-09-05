N = int(input("insira a quantidade de números reais: "))
somaReais = 0

nAtual = 0
while nAtual < N:
  somaReais += float(input(f"insira o {nAtual + 1}º número real da soma: "))
  nAtual += 1

print(f'soma dos valores: {somaReais}')