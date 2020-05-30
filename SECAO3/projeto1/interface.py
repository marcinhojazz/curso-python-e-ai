from tkinter import *

janela = Tk()
janela.title('Curso de Python')
janela.geometry('300x300')
janela.resizable(False, False)

Label(
    janela, 
    text='Texto dentro da janela', 
    bg='black', 
    fg='white',
    pady='30',
    padx=30
    ).grid(row=0, column=0)

janela.mainloop()
