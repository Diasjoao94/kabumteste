from sql_alchemy import banco


class ProdutoModel(banco.Model):
    __tablename__ = 'produtos'

    codigo = banco.Column(banco.Integer, primary_key=True)
    preco = banco.Column(banco.Float(precision=1))
    preco_prime = banco.Column(banco.Float(precision=2))
    preco_desconto = banco.Column(banco.Float(precision=3))
    preco_desconto_prime = banco.Column(banco.Float(precision=4))
    preco_antigo = banco.Column(banco.Float(precision=5))

    def __init__(self, codigo, preco, preco_prime, preco_desconto, preco_desconto_prime, preco_antigo):
        self.codigo = codigo
        self.preco = preco
        self.preco_prime = preco_prime
        self.preco_desconto = preco_desconto
        self.preco_desconto_prime = preco_desconto_prime
        self.preco_antigo = preco_antigo

    def json(self):
        return {
            'codigo': self.codigo,
            'preco': self.preco,
            'preco_prime': self.preco_prime,
            'preco_desconto': self.preco_desconto,
            'preco_desconto_prime': self.preco_desconto_prime,
            'preco_antigo': self.preco_antigo
        }

    @classmethod
    def find_produto(cls, codigo):
        produto = cls.query.filter_by(codigo=codigo).first()
        if produto:
            return produto
        return None

    def save_produto(self):
        banco.session.add(self)
        banco.session.commit()

    def update_produto(self, preco, preco_prime, preco_desconto, preco_desconto_prime, preco_antigo):
        self.preco = preco
        self.preco_prime = preco_prime
        self.preco_desconto = preco_desconto
        self.preco_desconto_prime = preco_desconto_prime
        self.preco_antigo = preco_antigo

    def delete_produto(self):
        banco.session.delete(self)
        banco.session.commit()
