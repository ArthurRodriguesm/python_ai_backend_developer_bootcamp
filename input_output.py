nome = input("Digite o seu nome: ")
idade = input("Agora digite a sua idade: ")

print(f"Olá, {nome}!")
print(f"Olá, {nome}", end="!\n")
print(nome, idade, sep=" tem ", end=" anos de idade \n") # Adicionando separador e finalização