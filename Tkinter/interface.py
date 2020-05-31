from tkinter import *

def mostrar():
    # pass
    armazenarLabel['text'] = 'botão foi clicado'
    # outras funções 
        # print('olá pessoal')
        # x = 20 + 20
        # print(x)


janela = Tk()
janela.title('Curso de Python')
janela.geometry('300x300')
janela.resizable(False, False)

Button(
    janela,
    text='Clique aqui',
    bg='black',
    fg='white',
    height=10,
    width=20,
    command=mostrar
    ).grid(row=0, column=0)

armazenarLabel = Label(janela, text='ainda não foi clicado')
armazenarLabel.grid(row=1, column=0)

janela.mainloop()


# 49. Criando campos para entrada de dados - Entry
   # Entry(
    #     janela,
    #     bg='black',
    #     fg='orange',
    #     show='*'
    #      ).grid(row=0, column=0)

   # 48. Criando campos para textos - Label
    # Label(
    #     janela, 
    #     text='Texto dentro da janela', 
    #     bg='black', 
    #     fg='white',
    #     pady='30',
    #     padx=30
    #     ).grid(row=0, column=0)



