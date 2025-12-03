📦 Gestão de Produtos API

API desenvolvida em FastAPI para gerenciar produtos, categorias e operações de CRUD com integração a banco de dados PostgreSQL.


📘 Sobre o Projeto

Este projeto é uma API moderna construída com FastAPI, focada em simplicidade, performance e organização.
O objetivo é permitir o cadastro, listagem, atualização e remoção de produtos de forma rápida e segura.

🗂️ Estrutura do Projeto
gestao_produtos_api/
│── app/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   ├── routers/
│   │   ├── produtos.py
│   │   └── categorias.py
│   └── __init__.py
│── requirements.txt
│── README.md
│── venv/

🛠️ Tecnologias Utilizadas

Python 3.10+

FastAPI

Uvicorn

SQLAlchemy

PostgreSQL

Pydantic

Alembic (opcional)

🚀 Como Rodar o Projeto
1️⃣ Criar o ambiente virtual
python -m venv venv


Ativar no Git Bash:

source venv/Scripts/activate

2️⃣ Instalar dependências
pip install -r requirements.txt

3️⃣ Configurar o banco de dados

Edite o arquivo .env com suas credenciais:

DATABASE_URL=postgresql://usuario:senha@localhost:5432/nomedb

4️⃣ Rodar o servidor
uvicorn main:app --reload


Acesse no navegador:

👉 http://127.0.0.1:8000

👉 Documentação automática Swagger: http://127.0.0.1:8000/docs

👉 Documentação Redoc: http://127.0.0.1:8000/redoc

📮 Rotas Principais
📍 Produtos

GET /produtos – listar produtos

POST /produtos – criar produto

GET /produtos/{id} – buscar produto

PUT /produtos/{id} – atualizar

DELETE /produtos/{id} – remover

📍 Categorias (se existir)

Semelhantes às rotas de produtos.

📌 Funcionalidades

✔ CRUD completo
✔ Documentação automática
✔ Validação de dados com Pydantic
✔ Integração com PostgreSQL
✔ Estrutura organizada em módulos

👥 Participantes
Daniel Duarte-01847432
Wesley Gonçalves-01849581
Thalles Tadeu-01857106
Julio César-01847484

Crie uma branch:

git checkout -b minha-feature


Commit:

git commit -m "Minha nova feature"


Push:

git push origin minha-feature


Abra um Pull Request no GitHub

📄 Licença

Este projeto está sob licença MIT — fique à vontade para usar e modificar.
