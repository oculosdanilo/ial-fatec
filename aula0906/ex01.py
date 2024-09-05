N = int(input("insira o nº de termos: ")) - 1
Razao = int(input("insira a razão da P.G.: "))
PrimTermo = int(input("insira o primeiro termo da P.G.: "))

# lista de valores
listaPG = [PrimTermo]
nAtual = 0
while nAtual < N:
  termoAtual = listaPG[nAtual] * Razao
  listaPG.append(termoAtual)
  nAtual += 1

# string formatado
formatado = f'{PrimTermo}'
nFormatacaoAtual = 1
while nFormatacaoAtual < len(listaPG):
  formatado += f' {listaPG[nFormatacaoAtual]}'
  nFormatacaoAtual += 1

# soma de todos os valores
soma = PrimTermo
nSomaAtual = 1
while nSomaAtual < len(listaPG):
  soma += listaPG[nSomaAtual]
  nSomaAtual += 1

print(formatado)
print(f'soma dos valores: {soma}')