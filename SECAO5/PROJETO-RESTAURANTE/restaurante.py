from tkinter import *

class JanelaLogin():
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

        self.senha = Entry(self.root)
        self.senha.grid(row=2, column=1, padx=5, pady=5)

        Button(self.root, text='login', bg='green3', width=10).grid(row=3, column=0, padx=5, pady=5)

        Button(self.root, text='cadastrar', bg='orange3', width=10).grid(row=3, column=1, padx=5, pady=5)

        Button(self.root, text='Visualizar cadastros', bg='white').grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        self.root.mainloop()

JanelaLogin()










# EXEMPLOS DE USO:

# class JanelaLogin():
    
    # def __init__(self):
    #     self.x = 10
        # print(self.x)

    # def mostrar(self):
    #     x = 20
    #     print(self.x)
    
    # def __init__(self):
    #     print('olá pessoal')

    # def mostrar(self):
    #     print('outra função')

# JanelaLogin()
# JanelaLogin().mostrar()