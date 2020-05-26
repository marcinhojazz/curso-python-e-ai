import pymysql.cursors

conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='interacaopython',
    charset='utf8mb4',
    cursorclass = pymysql.cursors.DictCursor

)



# # forma 1 de consulta
# with conexao.cursor() as cursor:
#     cursor.execute('select * from cadastros')
#     resultado = cursor.fetchall()

# # print(resultado)

# for dado in resultado:
#     # print(dado)
#     # print(dado['nome'])
#     # print(dado['nome'], dado['endereco'])
#     # print(dado['nome'] + ' | ' + dado['endereco'])
#     print('o nome do cliente é {} e mora no endereço {}'.format(dado['nome'], dado['endereco']))


# forma 2 de consulta
with conexao.cursor() as cursor:
    cursor.execute('select nome from cadastros')
    resultado = cursor.fetchall()

# print(resultado)

for dado in resultado:
    print(dado)