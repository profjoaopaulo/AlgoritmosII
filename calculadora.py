#CALCULADORA - Questão criada em aula para exemplo de uso de múltiplas Funções

#Função somar
def somar(x, y):
  return x + y

#Função subtrair
def subtrair(x, y):
  return x - y

#Função multiplicar
def multiplicar(x, y):
  return x * y

#Função dividir
def dividir(x, y):
  return x / y

#Função Resto de divisão
def resto(x, y):
  return x % y

#Main
a = float( input("Digite o primeiro valor: ") )
b = float( input("Digite o segundo valor: ") )

opInvalido = True

while opInvalido:
  print("Escolha a operação a se fazer:")
  print("Digite + para somar;")
  print("Digite - para subtrair;")
  print("Digite * para multiplicar;")
  print("Digite / para dividir.")
  print("Digite % para obter o resto da divisão.")
  operacao = input() #Lendo a operação
  if operacao == '+' or operacao == '-' or operacao == '*' or operacao == '/' or operacao == '%':
    opInvalido = False

if operacao == '+':
  print("Resultado = %.2f" % somar(a, b))
elif operacao == '-':
  print("Resultado = %.2f" % subtrair(a, b))
elif operacao == '*':
  print("Resultado = %.2f" % multiplicar(a, b))
elif operacao == '/':
  print("Resultado = %.2f" % dividir(a, b))
elif operacao == '%':
  print("Resultado = %.2f" % resto(a, b))

#Desafio: tentem implementar mais operações matemáticas, por exemplo, a potenciação

