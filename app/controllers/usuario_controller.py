from app.models.produto_model import UsuarioModel

class UsuarioController:
    def __init__(self):
        self.model = UsuarioModel()

    def autenticar(self, nome, senha):
        return self.model.autenticar(nome, senha)
