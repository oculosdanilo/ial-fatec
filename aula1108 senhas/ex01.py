# pdf: https://www.clictec.com.br/ial002m/aulas/IAL002_PrjN2B_2024.2_Senhas.pdf
# Projeto Senhas - 08/11
#   Antonio Marcos Freitas da Silva
#   Danilo Carvalho Lima
#   Marina Gusmão Faria Barbosa Bueno
#   Vinicius Coutinho de Castro

from random import randint, choice


def GerarSenha(Tipo, Tamanho):
  Contador = 0
  SenhaFinal = ""
  while Contador < Tamanho:
    match Tipo:
      case "A":
        SenhaFinal += str(randint(0, 9))
      case "B":
        Maiusculo = chr(randint(65, 90))
        Minusculo = chr(randint(97, 122))
        SenhaFinal += choice([Maiusculo, Minusculo])
      case "C":
        Maiusculo = chr(randint(65, 90))
        Algarismo = str(randint(0, 9))
        SenhaFinal += choice([Maiusculo, Algarismo])
      case "D":
        Maiusculo = chr(randint(65, 90))
        Minusculo = chr(randint(97, 122))
        Algarismo = str(randint(0, 9))
        SenhaFinal += choice([Maiusculo, Minusculo, Algarismo])
      case _:
        Maiusculo = chr(randint(65, 90))
        Minusculo = chr(randint(97, 122))
        Algarismo = str(randint(0, 9))
        SenhaFinal += choice(
          [Maiusculo, Minusculo, Algarismo, '+', '-', '_', '!', '?', '#', '@', '*', '&', '=', '$', '%'])

    Contador += 1

  return SenhaFinal


print('Tipos disponíveis:\n'
      'A. Numérica\n'
      'B. Alfabética\n'
      'C. Alfanumérica 1\n'
      'D. Alfanumérica 2\n'
      'E. Geral\n')

TipoSenha = input("Digite o tipo de senha que deve ser gerada: ")
while TipoSenha != "A" and TipoSenha != "B" and TipoSenha != "C" and TipoSenha != "D" and TipoSenha != "E":
  print("Tipo de senha inválido")
  TipoSenha = input("Digite o tipo de senha que deve ser gerada: ")

TamanhoSenha = int(input("Digite o tamanho das senhas: "))
while not (6 <= TamanhoSenha <= 25):
  if TamanhoSenha < 6:
    print("O tamanho deve ser igual ou maior que 6")
  else:
    print("O tamanho deve ser igual ou menor que 25")

  TamanhoSenha = int(input("Digite o tamanho das senhas: "))

ArquivoMatr = open("MATR.TXT", "r")
LinhaLida = ArquivoMatr.readline()
Matriculas = []
while LinhaLida != "" and LinhaLida != "\n":
  Matriculas.append(LinhaLida.strip())
  LinhaLida = ArquivoMatr.readline()
ArquivoMatr.close()

Senhas = ""
for Matricula in Matriculas:
  Senhas += f"{Matricula};{GerarSenha(TipoSenha, TamanhoSenha)};\n"

ArquivoSenhas = open("SENHAS.TXT", "w")
ArquivoSenhas.write(Senhas)
ArquivoSenhas.close()
