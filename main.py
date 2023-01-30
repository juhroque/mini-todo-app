import tkinter as tk

class AppTarefas():
    def __init__(self, janela):
        self.janela = janela
        self.janela.title('Gerenciador de Tarefas')
        self.janela.geometry('500x300')

        self.tarefas = tk.Listbox(width=50)
        self.tarefas.grid(column=1, row=3)

        self.label_tarefa = tk.Label(text='Tarefa:')
        self.label_tarefa.grid(column=0, row=0)
        
        self.entry_tarefa = tk.Entry(width=30)
        self.entry_tarefa.grid(column=1, row=0)

        self.botao_adicionar = tk.Button(text='Adicionar tarefa', command=self.add_tarefa)
        self.botao_adicionar.grid(column=1, row=2)

        self.botao_deletar = tk.Button(text='Deletar tarefa selecionada', command=self.deletar_tarefa, anchor='center')
        self.botao_deletar.grid(column=2, row=3)

    def add_tarefa(self):
        tarefa = self.entry_tarefa.get()
        self.tarefas.insert(tk.END, tarefa)

    def deletar_tarefa(self):
        tarefa = self.tarefas.curselection()
        self.tarefas.delete(tarefa)


# inicializa a janela:
root = tk.Tk()
app =  AppTarefas(root)

# fecha o loop da janela
root.mainloop()