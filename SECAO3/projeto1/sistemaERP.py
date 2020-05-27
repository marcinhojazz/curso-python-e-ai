import pymysql.cursors

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='erp',
    charset='utf8mb4',
    cursorclass = pymysql.cursors.DictCursor

)

authentication = False

while not authentication:
    decision = int(input('digite 1 para logar e 2 para cadastrar: '))

    try:
        with connection.cursor() as cursor:
            cursor.execute('select * from cadastros')
            result = cursor.fetchall()
            print(result)

    except:
        print('erro ao conectar ao DB')
