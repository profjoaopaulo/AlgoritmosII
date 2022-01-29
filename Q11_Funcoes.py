#Questão 11 (Funções)
def converteData(data):
  lista = data.split("/")
  meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
  return lista[0] + " de " + meses[ int(lista[1]) -1 ] + " de " + lista[2]

#Main
d = input("Digite uma data válida no formato dd/mm/aaaa: ")
dataExtenso = converteData(d)
print(dataExtenso)

