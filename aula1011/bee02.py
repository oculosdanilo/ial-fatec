m, n = map(int, input().split())

while m > 0 and n > 0:
  listaNum = []
  soma = 0

  if m > n:
    contN = n
    while contN <= m:
      listaNum.append(contN)
      soma += contN

      contN += 1

  else:
    contM = m
    while contM <= n:
      listaNum.append(contM)
      soma += contM

      contM += 1

  print(f'{listaNum} Sum={soma}'.replace(",", "").replace("[", "").replace("]", ""))
  m, n = map(int, input().split())