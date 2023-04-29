from tkinter import *
from tkinter import messagebox

def verificaçao():
    lista = list()
    lista.extend([(valores1.get()),float(valores2.get()),float(valores3.get()),float(valores4.get()),float(valores5.get()),
    float(valores6.get()),float(valores7.get()),float(valores8.get()),float(valores9.get()),float(valores10.get()),float(valores11.get()),float(valores12.get())])
    valor_veri = float(valor_verificaçao.get())
    if valor_veri in lista:
        messagebox.showinfo('INFORMAÇÃO','O VALOR ESTÁ NA MATRIZ !')
    else:
        messagebox.showinfo('INFORMAÇÃO',' NÃO ESTÁ NA MATRIZ !')
janela = Tk()
janela.title('VERIFICAÇÃO DE UM VALOR')
janela.geometry('200x310')
janela.maxsize(width=200, height=350)
LabelValor = Label(janela, text='VALORES').pack()
valores1 = Entry(janela)
valores1.place(x=20, y=30, relwidth= '0.2',relheight='0.1')
valores2 = Entry(janela)
valores2.place(x=20, y=71, relwidth= '0.2', relheight='0.1')
valores3 = Entry(janela)
valores3.place(x=20, y=111, relwidth= '0.2', relheight='0.1')
valores4 = Entry(janela)
valores4.place(x=20, y=151, relwidth= '0.2', relheight='0.1')
valores5 = Entry(janela)
valores5.place(x=80, y=30, relwidth= '0.2',relheight='0.1')
valores6 = Entry(janela)
valores6.place(x=80, y=71, relwidth= '0.2', relheight='0.1')
valores7 = Entry(janela)
valores7.place(x=80, y=111, relwidth= '0.2', relheight='0.1')
valores8 = Entry(janela)
valores8.place(x=80, y=151, relwidth= '0.2', relheight='0.1')
valores9 = Entry(janela)
valores9.place(x=140, y=30, relwidth= '0.2',relheight='0.1')
valores10 = Entry(janela)
valores10.place(x=140, y=71, relwidth= '0.2', relheight='0.1')
valores11 = Entry(janela)
valores11.place(x=140, y=111, relwidth= '0.2', relheight='0.1')
valores12 = Entry(janela)
valores12.place(x=140, y=151, relwidth= '0.2', relheight='0.1')

Label(janela).place(x=20, y=181)
Labelverificar = Label(janela,text='VALOR PARA VERIFICAÇÃO').place(x=30, y=201)

valor_verificaçao = Entry(janela)
valor_verificaçao.place(x=80, y=231, relwidth= '0.2', relheight='0.1')
botao = Button(janela, text='VERIFICAR', command=verificaçao).place(x=65, y=271)
janela.mainloop()