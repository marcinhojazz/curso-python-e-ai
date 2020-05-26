import pymysql.cursors

conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='interacaopython',
    charset='utf8mb4',
    cursorclass = pymysql.cursors.DictCursor

)

# variáveis popssíveis
# x = 'nadyra'

x = input('digite seu nome: ')
y = input('digite seu endereco: ')

with conexao.cursor() as cursor:
    # cursor.execute('insert into teste values("marcio");')
    # cursor.execute('insert into teste values("{}");'.format('andreia'))
    # cursor.execute('insert into teste values("{}");'.format(x)) #com a variável expressada acima e marcada com **
    
    # cursor.execute('create table cadastros( id int primary key auto_increment, nome varchar(50) not null, endereco varchar(100));')
    cursor.execute('insert into cadastros(nome, endereco) values ("{}", "{}")'.format(x, y))

    conexao.commit()
