# Gestão de Produtos API

API REST desenvolvida em **Python** com **FastAPI** e **PostgreSQL** para gerenciamento de produtos e categorias.

## Sobre o projeto

Projeto acadêmico desenvolvido em equipe com foco na construção de uma API organizada por camadas, operações CRUD, validação de dados e integração com banco de dados relacional.

## Tecnologias

- Python 3.10+
- FastAPI
- Uvicorn
- SQLAlchemy
- PostgreSQL
- Pydantic
- Alembic

## Estrutura

```text
gestao_produtos_api/
├── app/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   ├── routers/
│   │   ├── produtos.py
│   │   └── categorias.py
│   └── __init__.py
├── requirements.txt
└── README.md
```

## Funcionalidades

- CRUD de produtos
- CRUD de categorias
- Validação de dados com Pydantic
- Persistência em PostgreSQL
- Mapeamento de dados com SQLAlchemy
- Documentação automática da API com Swagger e ReDoc

## Como executar

### 1. Criar o ambiente virtual

```bash
python -m venv venv
```

No Windows (PowerShell):

```powershell
.\venv\Scripts\Activate.ps1
```

### 2. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 3. Configurar o banco de dados

Crie um arquivo `.env` com a URL de conexão do PostgreSQL, conforme a configuração utilizada pelo projeto. Não publique credenciais reais no repositório.

Exemplo:

```env
DATABASE_URL=postgresql://usuario:senha@localhost:5432/nomedb
```

### 4. Iniciar a API

```bash
uvicorn app.main:app --reload
```

A API ficará disponível em `http://127.0.0.1:8000`.

Documentação:

- Swagger: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Principais endpoints

### Produtos

| Método | Endpoint | Descrição |
|---|---|---|
| GET | `/produtos` | Lista produtos |
| POST | `/produtos` | Cria produto |
| GET | `/produtos/{id}` | Busca produto por ID |
| PUT | `/produtos/{id}` | Atualiza produto |
| DELETE | `/produtos/{id}` | Remove produto |

### Categorias

Possuem operações equivalentes para cadastro, consulta, atualização e remoção.

## Projeto acadêmico

Desenvolvido em equipe durante a formação em Análise e Desenvolvimento de Sistemas.
