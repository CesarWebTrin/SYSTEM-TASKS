#IMPORTAÇÃO DAS FUNÇÕES A SEREM UTILIZADAS DA BIBLIOTECA TKINTER

import tkinter as tk
import tkinter.ttk as tkk
from tkinter import messagebox

#IMPORTAÇÃO DO ARQUIVO DB

from db import *

#CRIAÇÃO DA CLASSE JANELA QUE VAI SER A RESONSÁVEL POR FAZER A EXIBIÇÃO GRÁFICA DO SISTEMA
class Janela(tk.Frame):
#CRIAÇÃO DO MÉTODO CONSTRUTOR QUE VAI EXIBIR A JANELA 
    def __init__(self, master=None):

        super().__init__(master)
        # Coletando informações do monitor
        largura = round(self.winfo_screenwidth() / 2)
        altura = round(self.winfo_screenheight() / 2)  
        tamanho = ('%sx%s' % (largura, altura))

        # Título da janela principal.
        master.title('System Tasks')
        # Tamanho da janela principal.
        master.geometry(tamanho)

        # Instanciando a conexão com o banco.
        self.db = ConectarDB()

         # Gerenciador de layout da janela principal.
        self.pack()

        # Criando os widgets da interface.
        self.criar_widgets()

    def criar_widgets(self):
        #Containers
        frame1 = tk.Frame(self)
        frame1.pack(side = tk.TOP, fill=tk.BOTH, padx=5, pady=5)

        frame2 = tk.Frame(self)
        frame2.pack(fill=tk.BOTH, expand=True)

        frame3 = tk.Frame(self)
        frame3.pack(side=tk.BOTTOM, padx=5, pady=5)

       #Labels

        label_tarefa = tk.Label(frame1, text='Descrição da Tarefa')
        label_tarefa.grid(row=0, column = 1)

        #Entrada de texto
        
        self.entry_tarefa = tk.Entry(frame1)
        self.entry_tarefa.grid(row=1, column=1, padx=0)

        #BOTÃO PARA ADICIONAR UM NOVO REGISTRO

        button_adicionar = tk.Button(frame1, text='Adicionar Tarefa', bg='blue', fg='white')
        #MÉTODO QUE É CHAMANDO QUANDO O BOTÃO É CLICADO
        button_adicionar['command'] = self.adicionar_tarefa
        button_adicionar.grid(row=0, column=3, rowspan=2, padx=10)

        #TREEVIEW

        self.treeview = tkk.Treeview(frame2, columns=('Código da Tarefa', 'Tarefa', 'Concluído'))
        self.treeview.heading('#0', text='ROWID')
        self.treeview.heading('#1', text='Código da tarefa')
        self.treeview.heading('#2', text='Tarefa')
        self.treeview.heading('#3', text='Concluído')

        #INSERINDO OS DADOS NO TREEVIEW

        for row in self.db.consultar_tarefas():
            self.treeview.insert('', 'end', text=row[0], values=(row[1], row[2], row[3]))

        self.treeview.pack(fill=tk.BOTH, expand=True)

        #BOTÃO PARA REMOVER UMA TAREFA
        button_excluir = tk.Button(frame3, text='Excluir', bg='red', fg='white')

        button_excluir['command'] = self.excluir_tarefa
        button_excluir.pack(pady=10)

        #BOTÃO PARA EDITAR UMA TAREFA

        button_update = tk.Button(frame3, text='Update', bg='green', fg='white')
        button_update['command'] = self.editar_tarefa
        button_update.pack(padx=5)

    def adicionar_tarefa(self):
        #COLEATANDO OS VALORES
        tarefa = self.entry_tarefa.get()
        
        try:
            #TAREFA DIGITADA É INSERIDA NO BANCO DE DADOS
            self.db.add_tarefa(tarefa=tarefa)

            #COLETANDO A ÚLTIMA ROWID QUE FOI INSERIDA NO BANCO DE DADOS
            rowid = self.db.consultar_ultimo_rowid()[0]

            #ADICIONANDO OS NOVOS DADOS NO TREEVIEW
            self.treeview.insert('', 'end', text=rowid, values=(rowid, tarefa, 'PENDENTE'))
        except Exception:
            exit(0)

    def excluir_tarefa(self):
        #VALIDAÇÃO PARA SABER SE O ITEM ESTÁ SELECIONADO 
        if not self.treeview.focus():
            messagebox.showerror('Erro', 'Nenhum intem selecionado')
        else :
            #COLETANDO QUAL ITEM ESTÁ SELECIONADO
            item_selecionado = self.treeview.focus()

            #COLETANDO OS DADOS DO ITEM SELECIONADO
            rowid = self.treeview.item(item_selecionado)

            #REMOVENDO O ITEM COM BASE NO VALOR DO ROWID
            #REMOVENDO UM VALOR DA TABELA 
            self.db.remover_tarefa(rowid['text'])

            #REMOVENDO O VALOR DO TREEVIEW
            self.treeview.delete(item_selecionado)

    def editar_tarefa(self):
        #VALIDAÇÃO PARA SABER SE O ITEM ESTÁ SELECIONADO 
        if not self.treeview.focus():
            messagebox.showerror('Erro', 'Nenhum intem selecionado')
        else :
             #COLETANDO QUAL ITEM ESTÁ SELECIONADO
            item_selecionado = self.treeview.focus()

            #COLETANDO OS DADOS DO ITEM SELECIONADO
            rowid = self.treeview.item(item_selecionado)

            #EDITANDO O ITEM COM BASE NO VALOR DA ROWID
            #DANDO UM UPDATE NA TABELA
            self.db.concluir_tarefa(rowid['text'])

            self.treeview.delete(item_selecionado)
            
"""  #ATUALIZANDO O TREEVIEW 
    for row in self.db.consultar_tarefas():
        self.treeview.insert('', 'end', text=row[0], values=(row[1], row[2], row[3])) """

    

root = tk.Tk()
app = Janela(master=root)
app.mainloop()