#Questão 03 (Funções)
def somaValores(x, y, z):
  return x + y + z

#main
a = float( input("valor 1: ") )
b = float( input("valor 2: ") )
c = float( input("valor 3: ") )

print("A soma dos valores digitados é: %.2f" % somaValores(a, b, c) )

