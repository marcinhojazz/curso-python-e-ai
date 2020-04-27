# RESOLUÇÃO DO EXERCÍCIO

nome = input('Digite seu nome: ')
idade = int(input('digite sua idade: '))
n1 = int(input('digite a nota da primeira prova: '))
n2 = int(input('digite a nota da segunda prova: '))

media = (n1 + n2) / 2
nome = nome.lower().title()

if media >= 6 and idade >= 18:
    print('{} Você passou!'.format(nome))
else: 
    print('{} foi reprovado'.format(nome))