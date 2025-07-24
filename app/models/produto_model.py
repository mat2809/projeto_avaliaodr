from app.database.conexao import conectar

class ProdutoModel:
    def __init__(self):
        self.conn = conectar()
        self.cursor = self.conn.cursor()

    def cadastrar(self, nome, preco, estoque):
        self.cursor.execute("INSERT INTO produtos (nome, preco, estoque) VALUES (%s, %s, %s)", (nome, preco, estoque))
        self.conn.commit()

    def listar(self):
        self.cursor.execute("SELECT * FROM produtos")
        return self.cursor.fetchall()
