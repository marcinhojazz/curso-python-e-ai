# print('1\n1\n1\n1\n1')

# while condicao == True:

# while True:

#_________________
# x = 0

# while x < 10:
#     print('1')
#     x = x + 1

# print('acabou o laço')
#_________________


# decisao = 0

# while decisao !=3:
#     decisao = int(input('digite 1 para logar, 2 para cadastrar e 3 para sair'))
    
#     if decisao == 1:
#         print('logado')
#     elif decisao == 2:
#         print('cadastrando')

# print('Você saiu')

#_________________

decisao = 0

while True:
    decisao = int(input('digite 1 para logar, 2 para cadastrar e 3 para sair'))

    if decisao == 3:
        break

    if decisao == 1:
        print('logado')
    elif decisao == 2:
        print('cadastrando')
print('Você saiu!')
