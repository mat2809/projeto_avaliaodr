from app.database.conexao import conectar

class ProdutoModel:
    def __init__(self):
        self.conn = conectar()
        self.cursor = self.conn.cursor()

    def cadastrar_produto(self, nome, preco, estoque):
        sql = "INSERT INTO produtos (nome, preco, estoque) VALUES (%s, %s, %s)"
        self.cursor.execute(sql, (nome, preco, estoque))
        self.conn.commit()

    def listar_produtos(self):
        self.cursor.execute("SELECT * FROM produtos")
        return self.cursor.fetchall()

    def atualizar_estoque(self, produto_id, nova_qtd):
        sql = "UPDATE produtos SET estoque = %s WHERE id = %s"
        self.cursor.execute(sql, (nova_qtd, produto_id))
        self.conn.commit()
