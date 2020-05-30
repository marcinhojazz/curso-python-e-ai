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

def excluirProdutos():
    idDeletar = int(input('Digite o id referente ao produto que deseja apagar:\n'))

    try:
        with conexao.cursor() as cursor:
            cursor.execute('delete from produtos where id = {}'.format(idDeletar))
    except:
        print('erro ao excluir o produto')

def listarPedidos():
    pedidos = []
    decision = 0

    while decision != 2:
        pedidos.clear()

        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from pedidos')
                listaPedidos = cursor.fetchall()
        except:
            print('erro no banco de dados')
        for i in listaPedidos:
            pedidos.append(i)
            
        if len(pedidos) != 0:
            for i in range(0, len(pedidos)):
                print(pedidos[i])
        else:
            print('nenhum pedido foi feito!')

        decision = int(input('digite 1 para dar um produto como entregue e 2 para voltar'))

        if decision == 1:
            idDeletar = int(input('digite o id do pedido entregue:\n'))

            try:
                with conexao.cursor() as cursor:
                    cursor.execute('delete from pedidos where id = {}'.format(idDeletar))
                    print('produto dado como entregue')
            except:
                print('erro ao dar o pedido como entregue')

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
            decisaoUsuario = int(input('digite 0 para sair, 1 parar cadastrar produtos, 2 para listar produtos cadastrados, 3 para listar os pedidos:\n'))
            
            if decisaoUsuario == 1:
                cadastrarProdutos()
            elif decisaoUsuario == 2:
                listarProdutos()

                delete = int(input('digite 1 para excluir um produto e 2 para sair\n'))

                if delete == 1:
                    excluirProdutos()
            elif decisaoUsuario == 3:
                listarPedidos()

# FUNÇÃO PARA CADASTRAR PRODUTOS