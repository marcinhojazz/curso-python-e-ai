import pymysql.cursors

conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='erp',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor

)

autentico = False
#função que permite usuario se cadastrar e logar no software
def logarCadastrar():
    usuarioExistente = 0
    autenticado = False
    usuarioMaster = False

    if decisao == 1:
        nome = input('digite seu nome: ')
        senha = input('digite sua senha: ')

        for linha in resultado:
            if nome == linha['nome'] and senha == linha['senha']:
                if linha ['nivel'] == 1:
                    usuarioMaster = False
                elif linha['nivel'] == 2:
                    usuarioMaster == True
                autenticado = True
            else:
                autenticado = False

        if not autenticado:
            print('email ou senha errado')

    elif decisao == 2:
        print('Faça seu cadastro')
        nome = input('digite seu nome: ')
        senha = input('sigite sua senha: ')

        for linha in resultado:
            if nome == linha['nome'] and senha == linha['senha']:
                usuarioExistente = 1
        
        if usuarioExistente == 1:
            print('usuario ja cadastrado, tente um nome ou senha diferente')
        elif usuarioExistente == 0:
            try:
                with conexao.cursor() as cursor:
                    cursor.execute('insert into cadastros(nome, senha, nivel) values (%s, %s, %s)', (nome, senha, 1))
                    conexao.commit()
                print('usuario cadastrado com sucesso!')
            except:
                print('erro ao inserir os dados no banco')

    return autenticado, usuarioMaster

while not autentico:
    decisao = int(input('digite 1 para logar e 2 para cadastrar: '))

    try:
        with conexao.cursor() as cursor:
            cursor.execute('select * from cadastros')
            resultado = cursor.fetchall()
            # print(resultado)
    except:
        print('erro ao conectar no banco de dados')


    autentico, usuarioSupremo = logarCadastrar()


if autentico == True:
    print('autenticado')