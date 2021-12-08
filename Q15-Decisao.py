##Questão 15 da lista de 'Estruturas de Decisão'
#Obtendo as entradas
a = float(input("Digite o lado a do triângulo: "))
b = float(input("Digite o lado b do triângulo: "))
c = float(input("Digite o lado c do triângulo: "))

#Verificar se é triângulo, de acordo com os lados lidos
if (a+b > c) and (a+c > b) and (b+c > a):
    print("Os lados formam um triângulo!")
    if a == b and a == c: #Teste Equilátero
        print("Equilátero!")
    elif a == b or a == c or b == c: #Teste Isósceles
        print("Isósceles!")
    else: #É Escaleno!
        print("Escaleno!")
else:
    print("Os lados NÃO formam um triângulo!")


