maior = 0
menor = 0
quant = 0
media = 0
soma = 0

x = 1
while x > 0:
  x = int(input("insira um número inteiro: "))

  if x != 0:
    if x > maior:
      maior = x

    if x < menor or menor == 0:
      menor = x

    quant += 1
    soma += x
    media = soma / quant

print(f'o maior valor é {maior}')
print(f'o menor valor é {menor}')
print(f'foram digitados {quant} números')
print(f'a media dos números é {media}')
print(f'a soma de todos os números é {soma}')
