#Questão 01 dos slides de Matrizes
#matriz m vazia antes de começar
m = []
nlinhas = 3
ncolunas = 3

#leitura
for i in range(nlinhas):
  l = []
  for j in range(ncolunas):
    l.append( int(input("Digite elemento %i%i: " % (i,j))) )

  m.append(l) #adicionando a nova linha após leitura de elementos nas colunas na matriz m

#imprimido antes
print("Antes...")
for i in range(nlinhas):
  for j in range(ncolunas):
    print(m[i][j], end = " ")
  print()

k = float( input("Digite o escalar: ") )

#multiplicando a diagonal principal pelo escalar k
for i in range(nlinhas):
  m[i][i] *= k

#imprimido depois
print("Depois...")
for i in range(nlinhas):
  for j in range(ncolunas):
    print(m[i][j], end = " ")
  print()

