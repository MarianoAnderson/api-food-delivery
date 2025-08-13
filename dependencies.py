from fastapi import Depends, HTTPException
from main import SECRET_KEY, ALGOTRITHM, oauth2_schema
from models import db, Usuario
from sqlalchemy.orm import Session, sessionmaker # 'sessionmaker' é uma fábrica para criar objetos de sessão.
from jose import jwt, JWTError

def pegar_sessao():
    # Inicia um bloco try-finally, garantindo que a sessão será fechada mesmo se ocorrer um erro.
    try:
        # Cria uma classe de sessão usando 'sessionmaker'.
        # 'bind=db' conecta esta sessão à instância do seu banco de dados ('db').
        Session = sessionmaker(bind=db)
        # Instancia uma nova sessão. Esta é a conexão real com o banco de dados.
        session = Session()
        # 'yield session' faz com que a função retorne a sessão para o chamador, mas mantém o estado da função, permitindo que a execução continue após o chamador terminar.
        yield session
    # O bloco 'finally' é executado sempre, independentemente de ocorrer um erro ou não.
    finally:
        # Fecha a sessão do banco de dados, liberando os recursos.
        session.close()

def verificar_token(token: str = Depends(oauth2_schema), session: Session = Depends(pegar_sessao)):
    try:
        dict_info = jwt.decode(token, SECRET_KEY, ALGOTRITHM)
        id_usuario = int(dict_info.get("sub"))
    except JWTError:
        raise HTTPException(status_code=401, detail="Acesso Negado, verifique a validade do token")
    # verificar se o token é valido
    # extrair o id do ususario
    usuario = session.query(Usuario).filter(Usuario.id==id_usuario).first()
    if not usuario:
        raise HTTPException(status_code=401, detail="Acesso Negado")
    return usuario