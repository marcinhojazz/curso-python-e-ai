'''
faça um programa que mostre o resultado de n!

S! = 5 * 4 * 3 * 2 * 1

'''

x = int(input('Digite um valor:\n'))

fatorial = 1
for i in range(x, 0, -1):
    fatorial = fatorial * i

print(fatorial)