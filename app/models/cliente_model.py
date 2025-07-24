from app.database.conexao import conectar

class ClienteModel:
    def __init__(self):
        self.conn = conectar()
        self.cursor = self.conn.cursor()

    def cadastrar_cliente(self, nome, email):
        sql = "INSERT INTO clientes (nome, email) VALUES (%s, %s)"
        self.cursor.execute(sql, (nome, email))
        self.conn.commit()

    def listar_clientes(self):
        self.cursor.execute("SELECT * FROM clientes")
        return self.cursor.fetchall()
