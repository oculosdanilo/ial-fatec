# pdf: https://www.clictec.com.br/ial002m/aulas/IAL002_PrjN2A_2024.2_Chinelandia.pdf
print('Antonio Marcos Freitas da Silva')
print('Danilo Carvalho Lima')
print('Marina Gusmão Faria Barbosa Bueno')
print('Vinicius Coutinho de Castro')
print('Projeto Chinelândia - 10/11\n')

arquivo = open('1_in.txt', 'r')

NPC = int(arquivo.readline())  # pega o npc da primeira linha
listaPares = []

cont = 0
while cont < NPC:
  cont += 1

arquivo.close()
