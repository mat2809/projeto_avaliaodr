import tkinter as tk
from tkinter import messagebox

class LoginView:
    def __init__(self, master, callback_login_sucesso):
        self.master = master
        self.callback_login_sucesso = callback_login_sucesso

        tk.Label(master, text="Login", font=("Arial", 14)).pack(pady=10)

        tk.Label(master, text="Usuário").pack()
        self.entry_usuario = tk.Entry(master)
        self.entry_usuario.pack()

        tk.Label(master, text="Senha").pack()
        self.entry_senha = tk.Entry(master, show="*")
        self.entry_senha.pack()

        tk.Button(master, text="Entrar", command=self.login).pack(pady=10)

    def login(self):
        usuario = self.entry_usuario.get()
        senha = self.entry_senha.get()

        # Aqui você pode chamar UsuarioController para autenticar
        if usuario == "admin" and senha == "123":  # Simulação
            messagebox.showinfo("Sucesso", "Login bem-sucedido!")
            self.callback_login_sucesso()
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos.")
