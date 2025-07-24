import tkinter as tk

class ProdutoView:
    def __init__(self, master):
        self.master = master
        master.title("Cadastro de Produtos")
        master.geometry("300x220")

        tk.Label(master, text="Nome:").pack()
        self.nome_entry = tk.Entry(master)
        self.nome_entry.pack()

        tk.Label(master, text="Preço:").pack()
        self.preco_entry = tk.Entry(master)
        self.preco_entry.pack()

        tk.Label(master, text="Estoque:").pack()
        self.estoque_entry = tk.Entry(master)
        self.estoque_entry.pack()

        tk.Button(master, text="Cadastrar", command=self.cadastrar_produto).pack(pady=10)

    def cadastrar_produto(self):
        nome = self.nome_entry.get()
        preco = self.preco_entry.get()
        estoque = self.estoque_entry.get()
        print(f"Produto cadastrado: {nome}, R${preco}, estoque: {estoque}")
