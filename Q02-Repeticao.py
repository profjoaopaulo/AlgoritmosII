usuario = input("Usuário: ")
senha = input("Senha: ")

while usuario == senha:
  print("Erro! A senha não pode ser igual ao usuário!")
  usuario = input("Usuário: ")
  senha = input("Senha: ")

print("Muito bem! Valores de login cadastrados.")
