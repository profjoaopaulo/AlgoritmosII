#Questão 01 (Funções)
#declaração 
def triangular(n):
  for i in range(n):
    for j in range(i+1):
      print(i+1, end = ' ')
    print()

#main
x = int( input("Digite o tamanho da matriz triangular: "))
triangular(x) #chamada da função!
