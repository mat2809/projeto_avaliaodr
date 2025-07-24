import tkinter as tk

class ClienteView:
    def __init__(self, master):
        self.master = master
        master.title("Cadastro de Clientes")
        master.geometry("300x200")

        tk.Label(master, text="Nome:").pack()
        self.nome_entry = tk.Entry(master)
        self.nome_entry.pack()

        tk.Label(master, text="Email:").pack()
        self.email_entry = tk.Entry(master)
        self.email_entry.pack()

        tk.Button(master, text="Cadastrar", command=self.cadastrar_cliente).pack(pady=10)

    def cadastrar_cliente(self):
        nome = self.nome_entry.get()
        email = self.email_entry.get()
        print(f"Cliente cadastrado: {nome} - {email}")  # Aqui você chamaria o controller
