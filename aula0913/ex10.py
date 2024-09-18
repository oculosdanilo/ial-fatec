n = int(input("insira um número de termos da sequencia: "))
prim = int(input("insira o número mínimo: "))

anteantes = 0
antes = 1
fibbo = ""
isPrimeiroN = True

x = 2
while x < n:
  soma = antes + anteantes
  if soma > prim:
    if isPrimeiroN:
      fibbo = f"{soma}"
      isPrimeiroN = False
    else:
      fibbo += f", {soma}"

  anteantes = antes
  antes = soma

  x += 1

print(f"se N = {n} então a sequência é: {fibbo}")
