n = int(input("insira um número inteiro: "))

anteantes = 0
antes = 1
fibbo = "0, 1"

x = 2
while x < n:
  soma = antes + anteantes
  fibbo += f", {soma}"

  anteantes = antes
  antes = soma

  x += 1

print(f"se N = {n} então a sequência é: {fibbo}")
