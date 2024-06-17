file = open('arquivo.txt','r') # Abrindo arquivo
print(file.read()) # Lê todo o arquivo
print(file.readline()) # Lê apenas uma linha
print(file.readlines()) # Lê todo o arquivo e coloca em uma lista
file.close()