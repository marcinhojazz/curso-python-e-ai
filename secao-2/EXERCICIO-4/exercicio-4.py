'''
faça um programa que receba varias idades e calcule e mostre a media das idades. finalize o programa quando a entrada for igual a -1.
'''
x = 0
soma = 0
i = 0

while x != -1:
    x = int(input('Digite uma idade: '))
    if x != -1: #se x for diferente de - 1
        soma += x  # a soma é igual a ela mesma + X
        i += 1
    
# print(x/i)
print(soma/i)