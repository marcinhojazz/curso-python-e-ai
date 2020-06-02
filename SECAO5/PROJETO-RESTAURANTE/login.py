from tkinter import *
import pymysql
from tkinter import messagebox

class AdminJanela():
    def __init__(self):
        self.root = Tk()
        self.root.title('ADMIN')
        self.root.geometry('500x500')

        self.root.mainloop()

class JanelaLogin():

    def VerificaLogin(self):
        autenticado = False
        usuarioMaster = False

        try:
            conexao = pymysql.connect(
                host='localhost',
                user='root',
                password='',
                db='erp',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor

            )
        except:
            print('erro ao conectar no banco de dados')

        usuario = self.login.get()
        senha = self.senha.get()

        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from cadastros')
                resultados = cursor.fetchall()
        except:
            print('erro ao fazer a consulta')
        
        for linha in resultados:
            if usuario == linha['nome'] and senha == linha['senha']:
                if linha['nivel'] == 1:
                    usuarioMaster = False
                elif linha['nivel'] == 2:
                    usuarioMaster = True
                autenticado = True
                break
            else:
                autenticado = False

        if not autenticado:
            messagebox.showinfo('login', 'Email ou senha invalidos')
        
        if autenticado:
            self.root.destroy()
            if usuarioMaster:
                AdminJanela()
    
    def CadastroBackEnd(self):
        codigoPadrao = '123@h'

        if self.codigoSeguranca.get() == codigoPadrao:
            if len(self.login.get()) <= 20:
                if len(self.senha.get()) <= 50:
                    nome = self.login.get()

                    senha = self.senha.get()

                    try:
                        conexao = pymysql.connect(

                            host='localhost',
                            user='root',
                            password='',
                            db='erp',
                            charset='utf8mb4',
                            cursorclass='pymysql.cursors.DictCursor'
                        )
                    except:
                        print('erro ao conectar ao banco de dados')
                    
                    try:
                        with conexao.cursor() as cursor:
                            cursor.execute('insert into cadastros (nome, senha, nivel) values (%s, %s, %s)', (nome, senha, 1))
                            conexao.commit()
                        messagebox.showinfo('cadastro', 'Usuario cadastrado com sucesso!')
                    except:
                        print('erro ao inserir dados')

                else:
                    messagebox.showinfo('ERRO', 'Por favor, insira uma senha com 50 ou menos caracteres')
            else:
                messagebox.showinfo('ERRO', 'Por favor, insira um nome com 20 caracteres')
        else:
            messagebox.showinfo('ERRO', 'Erro no código de segurança')


    def Cadastro(self):
        Label(self.root, text='Chave de segurança').grid(row=3, column=0, pady=5, padx=5)
        self.codigoSeguranca = Entry(self.root, show='*')
        self.codigoSeguranca.grid(row=3, column=1, pady=5, padx=10)
        Button(self.root, text='Confirmar cadastros', width=15, bg='blue3', command=self.CadastroBackEnd).grid(row=4, column=0, columnspan=3, pady=5, padx=10)


    def __init__(self):
        self.root = Tk()
        self.root.title('Login')
        Label(self.root, text='Faça o login').grid(row=0, column=0, columnspan=2)
        # campo usuario
        Label(self.root, text='Usuario').grid(row=1, column=0)

        self.login = Entry(self.root)
        self.login.grid(row=1, column=1, padx=5, pady=5)
        # campo senha
        Label(self.root, text='Senha').grid(row=2, column=0)

        self.senha = Entry(self.root, show='*')
        self.senha.grid(row=2, column=1, padx=5, pady=5)

        Button(self.root, text='login', bg='green3', width=10, command=self.VerificaLogin).grid(row=5, column=0, padx=5, pady=5)

        Button(self.root, text='cadastrar', bg='orange3', width=10, command=self.Cadastro).grid(row=5, column=1, padx=5, pady=5)

        Button(self.root, text='Visualizar cadastros', bg='white').grid(row=6, column=0, columnspan=2,  padx=5, pady=5)

        self.root.mainloop()

JanelaLogin()