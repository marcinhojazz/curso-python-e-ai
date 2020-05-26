import pymysql.cursors

conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='interacaopython',
    charset='utf8mb4',
    cursorclass = pymysql.cursors.DictCursor

)

# cursor = conexao.cursor()

# x = 'drop table pessoas' # excluindo tabela pessoas criada na linha de código abaixo

# # cursor.execute('create table pessoas(nome varchar(30), idade int, endereco varchar(100));')
# cursor.execute(x)


# cursor.close()
# conexao.close()

x = 'create table teste1(nome varchar(10));'

with conexao.cursor() as cursor:
    cursor.execute(x)

print('saiu')
