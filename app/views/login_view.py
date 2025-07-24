import tkinter as tk
from tkinter import messagebox
from app.controllers.usuario_controller import UsuarioController

class LoginView:
    def __init__(self, master):
        self.master = master
        master.title("Login")

        self.label_usuario = tk.Label(master, text="Usuário:")
        self.label_usuario.pack()

        self.entry_usuario = tk.Entry(master)
        self.entry_usuario.pack()

        self.label_senha = tk.Label(master, text="Senha:")
        self.label_senha.pack()

        self.entry_senha = tk.Entry(master, show="*")
        self.entry_senha.pack()

        self.btn_login = tk.Button(master, text="Entrar", command=self.login)
        self.btn_login.pack()

    def login(self):
        nome = self.entry_usuario.get()
        senha = self.entry_senha.get()

        controller = UsuarioController()
        if controller.autenticar(nome, senha):
            messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
        else:
            messagebox.showerror("Erro", "Usuário ou senha inválidos.")
