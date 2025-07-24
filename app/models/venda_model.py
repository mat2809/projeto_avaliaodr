from app.database.conexao import conectar
from datetime import datetime

class VendaModel:
    def __init__(self):
        self.conn = conectar()
        self.cursor = self.conn.cursor()

    def registrar_venda(self, cliente_id, itens):
        total = sum(item['quantidade'] * item['preco_unitario'] for item in itens)
        data_venda = datetime.now()

        # Inserir venda
        self.cursor.execute(
            "INSERT INTO vendas (cliente_id, data_venda, total) VALUES (%s, %s, %s)",
            (cliente_id, data_venda, total)
        )
        venda_id = self.cursor.lastrowid

        # Inserir itens da venda
        for item in itens:
            self.cursor.execute(
                "INSERT INTO itens_venda (venda_id, produto_id, quantidade, preco_unitario) VALUES (%s, %s, %s, %s)",
                (venda_id, item['produto_id'], item['quantidade'], item['preco_unitario'])
            )

        self.conn.commit()
