#Questão 06 da lista de Matrizes (prof Vanessa)
res = open("resultados.txt", "r")
mres = [] #matriz que conterá todos os dados
nlinhas = 6
ncolunas = 11

lines = res.readlines() #retornando uma lista de strings
res.close()
#rodando pelas linhas
for i in range(nlinhas):
  linha = lines[i].split() #cada linha que tava como uma string inteira em lines, agora retorna como uma lista com elementos string
  for j in range(1, ncolunas):
    linha[j] = int(linha[j]) #conversão dos tempos de cada volta para inteiro
  mres.append( linha ) #adiciona 

tempoMenorVolta = 1000000
pessoaMenorVolta = mres[0][0]
voltaMenor = 1
somasTempo = []
pessoas = []
mediasVoltas = []

for i in range(nlinhas):
  soma = 0
  for j in range(1, ncolunas):
    #a)#Algoritmo para encontrar o menor valor
    if mres[i][j] < tempoMenorVolta:
      tempoMenorVolta = mres[i][j]
      pessoaMenorVolta = mres[i][0]
      voltaMenor = j

    #b)
    soma += mres[i][j]
  somasTempo.append( soma )
  pessoas.append( mres[i][0] )
  mediasVoltas.append( soma/10 )


#bubble sort (ordenação)
for i in range(nlinhas - 1):
  for j in range(i+1, nlinhas):
    if somasTempo[i] > somasTempo[j]:
      aux = somasTempo[i]
      somasTempo[i] = somasTempo[j]
      somasTempo[j] = aux
      temp = pessoas[i]
      pessoas[i] = pessoas[j]
      pessoas[j] = temp


#c)
media = 1000000
for i in range(nlinhas):
  if mediasVoltas[i] < media:
    media = mediasVoltas[i]

#Saídas:
#a)
print("\n\nMelhor volta: %s com %i segundos na volta nº %i" % (pessoaMenorVolta, tempoMenorVolta, voltaMenor))

#b)
print("\n\nClassificação: ")
for i in range(nlinhas):
  if i == 0:
    print( pessoas[i], " Campeão!!!" )
  else:
    print(pessoas[i])

#c)
print("\n\nA média de voltas mais rápida: %.2f" % media)

