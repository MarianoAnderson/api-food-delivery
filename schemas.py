# Importa `BaseModel` do Pydantic (classe base para criar modelos de dados e definir a estrutura de seus dados.).
from pydantic import BaseModel 
# Importa `Optional` do `typing` (para campos que podem ser nulos).
from typing import Optional, List

# Define a classe `UsuarioSchemas` (modelo Pydantic para dados de usuário).
class UsuarioSchema(BaseModel):
    nome: str
    email: str
    senha: str
    ativo: Optional[bool]
    admin: Optional[bool]

    # Configurações do modelo Pydantic.
    class Config:
        # Permite que o modelo seja criado a partir de atributos de objetos (ex: ORM).
        from_attributes = True

class PedidoSchema(BaseModel):
    id_usuario: int

    class Config:
        from_attributes = True

class LoginSchema(BaseModel):
    email: str
    senha: str

    class Config:
        from_attributes = True

class ItemPedidoSchema(BaseModel):
    quantidade: int
    sabor: str
    tamanho: str
    preco_unitario: float

    class Config:
        from_attributes = True

class ResponsePedidoSchema(BaseModel):
    id: int
    status: str
    preco: float
    itens: List[ItemPedidoSchema]

    class Config:
        from_attributes = True