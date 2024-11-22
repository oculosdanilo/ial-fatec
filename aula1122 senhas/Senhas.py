from random import randint

print('A. Numérica\nB. Alfabética\nC. Alfanumérica 1')
print('D. Alfanumérica 2\nE. Geral')

# Garante que o programa so ira
# Rodar se o usuario digitar o
# Tipo de senha correto e tamanho
# Correto.
VERI = 0
VERIN = 0
while VERI == 0 or VERIN == 0:

  # Garante que o tipo de senha inserido seja
  # O correto.
  if VERI == 0:
    TIPO = input("\nDigite o Tipo de senha:")
    if TIPO == 'A':
      VERI = 1
    elif TIPO == 'B':
      VERI = 1
    elif TIPO == 'C':
      VERI = 1
    elif TIPO == 'D':
      VERI = 1
    elif TIPO == 'E':
      VERI = 1
    else:
      print('Tipo de senha inválido')

  # Garante que o tamanho de senha inserido seja
  # O correto.
  if VERI == 1:
    TAM = int(input('Digite o Tamnho da senha:'))
    if TAM > 25:
      print('TAMANHO INVALIDO')
    elif TAM < 6:
      print('TAMANHO INVALIDO')
    else:
      VERIN = 1

NDI = []
NDIS = []
QUAN = 0

# Abre o arquivo e separa cada linha em
# um elemento de cada lista.
file = open("MATR.TXT", 'r')
for i in file:
  NDI.append(i.strip())
file.close()

# Dicionario para os elementos especiais,
# Foi feito para maior facilidade
ELEMENTOS = {
  1: '+',
  2: '-',
  3: '_',
  4: '!',
  5: '?',
  6: '#',
  7: '@',
  8: '*',
  9: '&',
  10: '=',
  11: '$',
  12: '%'
}


# Função que gera senhas
def GeraSenha(TIPO, TAM):
  SENHA = ''
  if TIPO == 'A':
    for i in range(TAM):
      NA = randint(0, 9)
      SENHA += str(NA)


  elif TIPO == 'B':
    for i in range(TAM):
      NA = randint(1, 2)
      if NA == 1:
        NA = randint(65, 90)
        SENHA += chr(NA)
      elif NA == 2:
        NA = randint(97, 122)
        SENHA += chr(NA)


  elif TIPO == 'C':
    for i in range(TAM):
      NA = randint(1, 2)
      if NA == 1:
        NA = randint(65, 90)
        SENHA += chr(NA)
      elif NA == 2:
        NA = randint(0, 9)
        SENHA += str(NA)


  elif TIPO == 'D':
    for i in range(TAM):
      NA = randint(1, 3)
      if NA == 1:
        NA = randint(65, 90)
        SENHA += chr(NA)
      elif NA == 2:
        NA = randint(0, 9)
        SENHA += str(NA)
      elif NA == 3:
        NA = randint(97, 122)
        SENHA += chr(NA)


  elif TIPO == 'E':
    for i in range(TAM):
      NA = randint(1, 4)
      if NA == 1:
        NA = randint(65, 90)
        SENHA += chr(NA)
      elif NA == 2:
        NA = randint(97, 122)
        SENHA += chr(NA)
      elif NA == 3:
        NA = randint(0, 9)
        SENHA += str(NA)
      elif NA == 4:
        NA = randint(1, 12)
        SENHA += ELEMENTOS[NA]
  return SENHA


# Usando a função que gera senha, eu crio uma
# Lista contendo o 'RA' e a senha
for i in NDI:
  NDIS.append(i)
  NDIS.append(GeraSenha(TIPO, TAM))

# Eu escrevo no documento o texto formatando
# ele, utilizando o loop for
file = open('SENHAS.TXT', 'w')
for i in NDIS:
  file.write(i)
  file.write(';')
  QUAN += 1
  if QUAN == 2:
    file.write('\n')
    QUAN = 0
file.close()
print(NDIS)
