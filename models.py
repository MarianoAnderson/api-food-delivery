                        # criar tabela e tudo que eu vou usar para construir a tabela
from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
                #  função que cria uma classe base, através classes python, para suas classes de modelo de banco de dados.
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy_utils.types import ChoiceType # Impede a inscrição de outra coisa antes ja citada no banco de dados

# cria a conexão do seu banco
db = create_engine("sqlite:///banco.db")

# cria a base do banco de dados
Base = declarative_base()

# criar as classes/tabelas do banco
class Usuario(Base):

    # colocando nome da tabela
    __tablename__ = "usuarios"

    # criano e passando as informações da tabela
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String, nullable=False)
    email = Column("email", String, nullable=False)
    senha = Column("senha", String, nullable=False)
    ativo = Column("ativo", Boolean)
    admin = Column("admin", Boolean, default=False)

    # criando a função python
    def __init__ (self, nome, email, senha, ativo=True, admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin

class Pedido(Base):
    __tablename__ = "pedidos"

    # lista de tupla que o ChoiceType necessita para armazenar o status permanente a ser utilizado 
    # STATUS_PEDIDO = (
    #     ("PENDENTE", "PENDENTE"),
    #     ("cANCELADO", "CANCELADO"),
    #     ("FINALIZADO", "FINALIZADO")
    # )

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    # status = Column("status", ChoiceType(choices=STATUS_PEDIDO)) # pendente, cancelado, finalizado
    status = Column("status", String)
    usuario = Column("usuario", ForeignKey("usuarios.id"))
    preco = Column("preco", Float)
    itens = relationship("ItemPedido", cascade="all, delete")

    def __init__ (self, usuario, status="PENDENTE", preco=0):
        self.status = status
        self.usuario = usuario
        self.preco = preco

    def calcular_preco(self):
        # percorrer todos os itens do pedido
        # somar todos os preços de todos os itens selecionados
        # editar no campo "preco" o valor final do preco do pedido
        self.preco = sum(item.preco_unitario * item.quantidade for item in self.itens)

class ItemPedido(Base):
    __tablename__ = "itens_pedido"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    quantidade = Column("quantidade", Integer)
    sabor = Column("sabor", String)
    tamanho = Column("tamanho", String)
    preco_unitario = Column("preco_unitario", Float)
    pedido = Column("pedido", ForeignKey("pedidos.id"))

    def __init__ (self, quantidade, sabor, tamanho, preco_unitario, pedido):
        self.quantidade = quantidade
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco_unitario = preco_unitario
        self.pedido = pedido

# execulta a criação dos metadados do seu banco (cria efetivamente o banco de dados)

# migrar o banco de dados

# criar a migração: alembic revision --autogenerate -m " "
# executar a migração: alembic upgrade head