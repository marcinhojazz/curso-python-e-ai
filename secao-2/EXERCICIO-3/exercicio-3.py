'''
faça um programa que verifique e mostre os números entre 1000 e 2000(inclusive) que, quando dividido por 11 produz resto igual a 5
'''

for i in range(1000, 2001):
    # print(i)
    if i % 11 == 5:
        print(i)