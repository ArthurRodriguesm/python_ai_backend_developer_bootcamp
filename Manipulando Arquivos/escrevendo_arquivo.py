file = open('arquivo.txt', 'w')
file.write('Seja bem-vindo(a)') # Escreve dentro do arquivo
file.writelines(['\n', "Write", '\n', 'lines']) # Escreve dentro de uma lista
file.close()