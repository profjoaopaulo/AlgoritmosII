#Questão 06 (Funções)
def amPM(hour):
  if hour < 12:
    return "A.M."
  else:
    return "P.M"

def conversao12H(horas, minutos):
  h12 = horas
  if horas > 12:
    h12 -= 12 #h12 = h12 - 12
  
  #chamada da função amPM() dentro da função conversao12H()
  return str(h12) + ":" + str(minutos) + " " + amPM(horas)

#Main
h = int( input("Horas(24H): ") )
m = int (input("Minutos: "))

print("São %s!" % conversao12H(h, m) )
