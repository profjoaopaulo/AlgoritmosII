#Questão 21 (Repetição)

x = int( input("Digite um número inteiro: ") )
ehPrimo = True

#Teste para saber se é primo
for i in range(2, x):
  if x % i == 0:
    ehPrimo = False
    break

if ehPrimo:
  print("O valor %i é primo" % x)
else:
  print("O valor %i NÃO é primo" % x)
