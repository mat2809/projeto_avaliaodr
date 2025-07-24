import tkinter as tk

class VendaView:
    def __init__(self, master):
        self.master = master
        master.title("Registro de Venda")
        master.geometry("300x200")

        tk.Label(master, text="ID do Cliente:").pack()
        self.cliente_id_entry = tk.Entry(master)
        self.cliente_id_entry.pack()

        tk.Label(master, text="ID do Produto:").pack()
        self.produto_id_entry = tk.Entry(master)
        self.produto_id_entry.pack()

        tk.Label(master, text="Quantidade:").pack()
        self.qtd_entry = tk.Entry(master)
        self.qtd_entry.pack()

        tk.Button(master, text="Registrar Venda", command=self.registrar_venda).pack(pady=10)

    def registrar_venda(self):
        cliente_id = self.cliente_id_entry.get()
        produto_id = self.produto_id_entry.get()
        qtd = self.qtd_entry.get()
        print(f"Venda registrada: Cliente {cliente_id}, Produto {produto_id}, Quantidade {qtd}")
