# AULA 14 | Tratamento de Exceções

try:
    x = int(input('digite sua idade: '))
except:
    print('Você não digitou sua idade')
else:
    print(f'sua idade é {x}')
finally:
    print('muito obrigado por digitar sua idade')