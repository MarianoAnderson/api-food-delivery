# 🍕 Backend FastAPI para Gerenciamento de Pedidos 🚀

Este projeto é uma API de backend robusta e eficiente, desenvolvida com FastAPI, projetada para gerenciar a autenticação de usuários e o processamento de pedidos. Ela fornece endpoints para 
registro de usuários, login, criação de pedidos, cancelamento e gerenciamento de itens. A aplicação utiliza JWT para autenticação segura e SQLAlchemy para interações com o banco de dados, 
garantindo a integridade e a segurança dos dados.

## 🚀 Principais Recursos

- **Autenticação de Usuário:** Registro e login seguros de usuários usando tokens JWT.
- **Gerenciamento de Pedidos:** Crie, cancele e liste pedidos.
- **Gerenciamento de Itens:** Adicione e remova itens de pedidos.
- **Controle de Acesso Baseado em Funções:** Usuários administradores podem listar todos os pedidos, enquanto usuários comuns podem gerenciar apenas seus próprios pedidos.
- **Validação de Dados:** Utiliza esquemas Pydantic para validação robusta de dados.
- **Migrações de Banco de Dados:** O Alembic é configurado para gerenciar alterações de esquema de banco de dados.
- **Injeção de Dependências:** O sistema de injeção de dependências do FastAPI é usado para gerenciamento de sessões de banco de dados e verificação de tokens.

## 🛠️ Pilha de Tecnologia

* **Estrutura de Backend:** FastAPI
* **Banco de Dados:** SQLite (com ORM SQLAlchemy)
* **Autenticação:** JWT (usando `python-jose`)
* **Hash de Senha:** bcrypt (via `passlib`)
* **Validação de Dados:** Pydantic
* **Migrações de Banco de Dados:** Alembic
* **Injeção de Dependência:** `Depends` da FastAPI
* **Variáveis de Ambiente:** `python-dotenv`
* **ORM:** SQLAlchemy
* **Ferramenta de Build:** pip

## 📦 Primeiros passos

Siga estes passos para configurar e executar o projeto localmente.

### Pré-requisitos

- Python 3.8+
- gerenciador de pacotes pip

### Instalação

1. **Clone o repositório:**

```bash
git clone <url_do_repositório>
cd <diretório_do_repositório>
```

2. **Crie um ambiente virtual (recomendado):**

```bash
python -m venv venv
source venv/bin/activate # No Linux/macOS
venv\Scripts\activate # No Windows
```

3. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

4. **Configure as variáveis de ambiente:**

Crie um arquivo `.env` no diretório raiz e adicione as seguintes variáveis:

```
CHAVE_SECRETA=Sua chave secreta aqui
ALGORITMO=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

5. **Execute migrações de banco de dados:**

```bash
alembic upgrade head
```

### Executando Localmente

1. **Inicie o servidor FastAPI:**

```bash
uvicorn main:app --reload
```

Isso iniciará o servidor em `http://127.0.0.1:8000`. A flag `--reload` habilita o recarregamento automático do servidor em caso de alterações no código.

2. **Acesse a documentação da API:**

Abra seu navegador e navegue até `http://127.0.0..1:8000/docs` para acessar a documentação da interface do usuário do Swagger gerada automaticamente.

## 📂 Estrutura do Projeto

```
.
├── alembic/
│ ├── versões/
│ │ └── ... (arquivos de migração)
│ ├── alembic.ini
│ └── env.py
├── auth_routes.py
├── dependencies.py
├── main.py
├── models.py
├── order_routes.py
├── README.md
├── requirements.txt
└── schemas.py
```

## 🤝 Contribuindo

Contribuições são bem-vindas! Siga estes passos:

1. Faça um fork do repositório.
2. Crie uma nova branch para o seu recurso ou correção de bug.
3. Faça suas alterações e envie-as com mensagens claras e descritivas.
4. Envie um pull request.

## 📝 License

This project is licensed under the [MIT License](LICENSE).

## 📬 Contato

Caso tenha alguma dúvida ou sugestão, entre em contato comigo pelo e-mail [andersonmariano801@gmail.com](andersonmariano801@gmail.com).

## 💖 Mensagem de Agradecimento

Obrigado por conferir este projeto! Espero que seja útil e que você o ache fácil de usar e contribuir.
