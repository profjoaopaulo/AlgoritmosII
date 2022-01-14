#Questão 07 (Decisão)


a = float(input("Digite um valor: "))
b = float(input("Digite outro valor: "))
c = float(input("Digite mais um valor: "))

#Maior...
if a > b and a > c:
  print("O valor %f é o maior!" % a)
elif b > c:
  print("O valor %f é o maior" % b)
else:
  print("O valor %f é o maior" % c)

#Menor...
if a < b and a < c:
  print("O valor %f é o menor!" % a)
elif b < c:
  print("O valor %f é o menor" % b)
else:
  print("O valor %f é o menor" % c)

#DESAFIO: ler 10 valores reais e informar o maior e o menor deles!
