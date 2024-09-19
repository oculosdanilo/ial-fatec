n = int(input())

cobaias = 0
coelhos = 0
ratos = 0
sapos = 0
i = 0
while i < n:
  cobaia = input()
  cobaia = cobaia.split()

  match cobaia[1]:
    case "C":
      coelhos += int(cobaia[0])
    case "R":
      ratos += int(cobaia[0])
    case "S":
      sapos += int(cobaia[0])

  cobaias += int(cobaia[0])

  i += 1

porcCoelhos = (coelhos / cobaias) * 100
porcRatos = (ratos / cobaias) * 100
porcSapos = (sapos / cobaias) * 100

print(f'Total: {cobaias} cobaias')
print(f'Total de coelhos: {coelhos}\nTotal de ratos: {ratos}\nTotal de sapos: {sapos}')
print(
  f'Percentual de coelhos: {porcCoelhos:.2f} %\nPercentual de ratos: {porcRatos:.2f} %\nPercentual de sapos: {porcSapos:.2f} %')
