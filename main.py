from fastapi import FastAPI
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from dotenv import load_dotenv
import os # Interação com os sistema operacional, como automoção de tarefas e gerenciamentos de arquivos e diretorios.

load_dotenv()

# Variaveis de ambiente: .env
SECRET_KEY = os.getenv("SECRET_KEY")
ALGOTRITHM = os.getenv("ALGOTRITHM")
#                             Variaveis de ambientes são istrings, necessario usar um int ou  float
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

app = FastAPI()

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_schema = OAuth2PasswordBearer(tokenUrl="auth/login-form")

from auth_routes import auth_router
from order_routes import order_router

app.include_router(auth_router)
app.include_router(order_router)




#Para rodar o nosso codigo, executar no terminal: uvicorn main:app --reload

# Rest APIs
# Get -> leitura/pegar
# Post -> enviar/criar
# Put/Patch -> edição
# Delete -> deletar