# arquivo = open('secao-2/aula19.txt', 'w') #sobreescreve o arquivo
# arquivo = open('secao-2/aula19.txt', 'a') #altera / adiciona mais um bloco de texto
arquivo = open('secao-2/aula19.txt', 'r') #Ler arquivo


# texto = '''
# Testando escrita de um texto.
# Meu nome é Márcio e sobreescreverei o arquivo
# e Mais uma linha nova para ver como fica
# '''


# texto = arquivo.read()
texto = arquivo.readlines()



# arquivo.write('Primeiro write')
# arquivo.write(texto)

# print(texto)

for i in texto:
    print(i)

arquivo.close