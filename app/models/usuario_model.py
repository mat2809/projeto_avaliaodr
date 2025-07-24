from app.database.conexao import conectar

class UsuarioModel:
    def __init__(self):
        self.conn = conectar()
        self.cursor = self.conn.cursor()

    def autenticar(self, nome, senha):
        sql = "SELECT * FROM usuarios WHERE nome = %s AND senha = %s"
        self.cursor.execute(sql, (nome, senha))
        return self.cursor.fetchone()

    def cadastrar_usuario(self, nome, senha):
        sql = "INSERT INTO usuarios (nome, senha) VALUES (%s, %s)"
        self.cursor.execute(sql, (nome, senha))
        self.conn.commit()
