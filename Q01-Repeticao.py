nota = float( input("Digite uma nota entre 0 e 10: ") )

while nota < 0 or nota > 10: #testa o valor inválido
    nota = float( input("Valor inválido! Digite uma nota entre 0 e 10: ") )

print("Ok, válido!")
print("Nota digitada: ", nota)
