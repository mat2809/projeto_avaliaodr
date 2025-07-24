import tkinter as tk
from app.views.login_view import LoginView
from app.views.menu_view import MenuView
from app.views.cliente_view import ClienteView
from app.views.produto_view import ProdutoView
from app.views.venda_view import VendaView

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Controle de Loja")
        self.abrir_login()

    def abrir_login(self):
        self.limpar_janela()
        LoginView(self.root, self.abrir_menu)

    def abrir_menu(self):
        self.limpar_janela()
        MenuView(self.root, self.abrir_clientes, self.abrir_produtos, self.abrir_vendas)

    def abrir_clientes(self):
        nova_janela = tk.Toplevel(self.root)
        ClienteView(nova_janela)

    def abrir_produtos(self):
        nova_janela = tk.Toplevel(self.root)
        ProdutoView(nova_janela)

    def abrir_vendas(self):
        nova_janela = tk.Toplevel(self.root)
        VendaView(nova_janela)

    def limpar_janela(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x300")
    app = App(root)
    root.mainloop()
