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
def logarCadastrar(decidir):

    usuarioExistente = 0
    autenticado = False
    usuarioMaster = False
    if decisao == 1:
        nome = input('digite seu nome:\n')
        senha = input('digite sua senha:\n')



        for linha in resultado:
            if nome == linha['nome'] and senha == linha['senha']:
                if linha ['nivel'] == 1:
                    usuarioMaster = False
                elif linha['nivel'] == 2:
                    usuarioMaster = True
                autenticado = True
                break
            else:
                autenticado = False

        if not autenticado:
            print('email ou senha errado')

    elif decisao == 2:
        print('Faça seu cadastro')
        nome = input('digite seu nome:\n')
        senha = input('sigite sua senha:\n')

        for linha in resultado:
            if nome == linha['nome'] and senha == linha['senha']:
                usuarioExistente = 1
        
        if usuarioExistente == 1:
            print('usuario ou senha ja existente!')
        elif usuarioExistente == 0:
            try:
                with conexao.cursor() as cursor:
                    cursor.execute('insert into cadastros(nome, senha, nivel) values (%s, %s, %s)', (nome, senha, 1))
                    conexao.commit()
                print('usuario cadastrado com sucesso!')
            except:
                print('erro ao inserir os dados no banco')

    return autenticado, usuarioMaster


def cadastrarProdutos():
    nome = input('digite o nome do produto')
    ingredientes = input('digite os ingredientes dos produtos:\n')
    grupo = input('digite o grupo pretencente a esse produto:\n')
    preco = float(input('digite o preço do produto:\n'))

    try:
        with conexao.cursor() as cursor:
            cursor.execute('insert into produtos (nome, ingredientes, grupo, preco) values (%s, %s, %s, %s)', (nome, ingredientes, grupo, preco))
            conexao.commit()
            print('produto cadastrado com sucesso')
    except:
        print('erro ao inserir os produtos no banco de dados')

def listarProdutos():
    produtos = []

    try:
        with conexao.cursor() as cursor:
            cursor.execute('select * from produtos')
            produtosCadastrados = cursor.fetchall()
            # print(produtosCadastrados)
    except:
        print('erro ao conectar no banco de dados')

    for i in produtosCadastrados:
        produtos.append(i)

    if len(produtos) != 0:
        for i in range(0, len(produtos)):
            print(produtos[i])
    else:
        print('nenhum produto cadastrado')

while not autentico:
    decisao = int(input('digite 1 para logar e 2 para cadastrar:\n'))

    try:
        with conexao.cursor() as cursor:
            cursor.execute('select * from cadastros')
            resultado = cursor.fetchall()
            # print(resultado)
    except:
        print('erro ao conectar no banco de dados')


    autentico, usuarioSupremo = logarCadastrar(decisao)




if autentico == True:
    print('autenticado')

    if usuarioSupremo == True:
        decisaoUsuario = 1
        

        while decisaoUsuario != 0: #enquanto decisaoUsuario for diferente de 0...
            decisaoUsuario = int(input('digite 0 para sair, 1 parar cadastrar produtos, 2 para listar produtos cadastrados'))
            
            if decisaoUsuario == 1:
                cadastrarProdutos()
            elif decisaoUsuario == 2:
                listarProdutos()

# FUNÇÃO PARA CADASTRAR PRODUTOS