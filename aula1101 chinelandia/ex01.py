# pdf: https://www.clictec.com.br/ial002m/aulas/IAL002_PrjN2A_2024.2_Chinelandia.pdf
# Projeto Chinelândia - 10/11
#   Antonio Marcos Freitas da Silva
#   Danilo Carvalho Lima
#   Marina Gusmão Faria Barbosa Bueno
#   Vinicius Coutinho de Castro

# estrutura dos dados finais: {<número do padrão> + " " + <lado do pé>: <quantos disponíveis para troca>}
#                         ex: {"3 D": 1}
dadosFinais = {}
listaJaContados = []  # lista que guarda os números ja contados, para não lê-los denovo e contar como mais de 1 vez repetidos


def existeNaListaJaContada(numero):  # retorna True se o numero ja está na lista, False se não estiver
  for jaContado in listaJaContados:
    if numero == jaContado:
      return True

  return False


def existeNosDadosFinais(chave):  # retorna True se a chave existir no dicionario, False se não existir
  for dadoChave in dadosFinais.keys():
    if chave == dadoChave:
      return True

  return False


# função generica que checa todos os chinelos de uma lista de um pé sem repetir os chinelos que ja foram comparados (A com B e B com A)
def checarPesRepetidos(lista, lado):
  A = 0  # A é o chinelo a ser comparado com B
  while A < len(lista) - 1:  # -1 para ignorar o último chinelo A que ja foi comparado com todos os anteriores

    B = 1 + A
    # o chinelo A será comparado a todos os chinelos depois de A, sendo esses B
    # assim, os chinelos a serem comparados serão, numa lista de 6 inputs:
    # 0 e 1, 0 e 2, 0 e 3, 0 e 4, 0 e 5
    # 1 e 2, 1 e 3, 1 e 4, 1 e 5
    # ...
    # 4 e 5

    while B < len(lista):
      if lista[A] == lista[B] and not existeNaListaJaContada(lista[A]):  # checa se há repetição
        if not existeNosDadosFinais(f'{lista[A]} {lado}'):
          # se não existir no dicionario uma entrada com esse número, criar uma
          dadosFinais[f'{lista[A]} {lado}'] = 1
        else:
          # se existir, só adicionar mais um ao número de disponíveis
          dadosFinais[f'{lista[A]} {lado}'] += 1

      if B == len(lista) - 1:
        listaJaContados.append(lista[A])
        # quando ja contado, o numero vai pra uma lista negra para não ser contado novamente

      B += 1

    A += 1


def sortLista(e):
  return int(e.split()[0])


arquivo = open('input.txt', 'r')  # abre o arquivo

NPC = int(arquivo.readline())  # pega o npc da primeira linha
listaE = []  # lista de pés esquerdos
listaD = []  # lista de pés direitos

contReadLines = 0
while contReadLines < NPC:  # lê todas as linhas do arquivo
  linhaAtual = arquivo.readline().split()

  listaE.append(int(linhaAtual[0]))  # append do pé esquerdo
  listaD.append(int(linhaAtual[1]))  # append do pé direito

  contReadLines += 1

arquivo.close()

checarPesRepetidos(listaE, "E")
listaJaContados = []
checarPesRepetidos(listaD, "D")

resultado = ""
if len(dadosFinais.keys()) == 0:  # checa se o
  resultado = "SEM TROCAS DESTA VEZ"
else:
  listaOrdenada = []
  for dado in dadosFinais.items():
    listaOrdenada.append(f'{dado[0]} {dado[1]}\n')

  # organiza a lista de valores com base no primeiro valor
  listaOrdenada.sort(key=sortLista)

  for item in listaOrdenada:
    resultado += item

output = open("output.txt", "w")
output.write(resultado)
output.close()
