
import tkinter as tk

class MenuView:
    def __init__(self, master, abrir_clientes, abrir_produtos, abrir_vendas):
        self.master = master
        tk.Label(master, text="Menu Principal", font=("Arial", 14)).pack(pady=10)

        tk.Button(master, text="Cadastro de Clientes", width=25, command=abrir_clientes).pack(pady=5)
        tk.Button(master, text="Cadastro de Produtos", width=25, command=abrir_produtos).pack(pady=5)
        tk.Button(master, text="Registro de Vendas", width=25, command=abrir_vendas).pack(pady=5)
        tk.Button(master, text="Sair", width=25, command=master.quit).pack(pady=20)
