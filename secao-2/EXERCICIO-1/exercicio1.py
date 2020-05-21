'''
Faça um programa que receba o peso de 7 pessoas. Calcule e mostre:
* a quantidade de pessoas acima de 90kgs
* a medida dos pesos das pessoas
'''

x = []
contador = 0
for i in range(0, 7):
    x.append(float(input('Digite um peso:\n ')))
    if x[i] > 90:

        contador += 1

# print(f'existem {contador} pessoas acima de 90kg e a media de todos os pesos é {sum(x)/len(x)}')
print(f'existem {contador} pessoas acima de 90kg e a media de todos os pesos é {sum(x)/len(x):.2f}kg')