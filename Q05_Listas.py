#Questão 05 (Listas)

numeros = []
pares = []
impares = []
#primos = []

#leitura dos 20 números
for i in range(20): #0 a 19
  print("Digite o valor %i" % (i+1) )
  numeros.append( int( input() ) )
  if numeros[i] % 2 == 0:
    pares.append( numeros[i] )
  else:
    impares.append( numeros[i] )

print("Numeros:", numeros)
print("Pares:", pares)
print("Impares:", impares)

#Adicionar ao problema uma Lista que vai guardar os números Primos

