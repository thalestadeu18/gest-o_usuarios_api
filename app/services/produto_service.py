from sqlalchemy.orm import Session
from models.produto_model import Produto

def criar_produto(db: Session, nome: str, valor: float, descricao: str, quantidade: int):

    produto_existente = db.query(Produto).filter(Produto.nome == nome).first()

    if produto_existente:
        raise ValueError("Produto já cadastrado no estoque!")

    novo_produto = Produto(
        nome=nome, 
        valor=valor, 
        descricao=descricao, 
        quantidade=quantidade
    )
    
    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)
    return novo_produto

def listar_produtos(db: Session):
    return db.query(Produto).all()
    
#Daniel: Função para deletar produto
def deletar_produto(db, produto_id: int):
    produto = db.query(Produto).filter(Produto.id == produto_id).first()
    if not produto:
        return False
    db.delete(produto)
    db.commit()
    return True
    
# Wesley: Função para atualizar o produto 
def atualizar_produto(db: Session, produto_id: int, nome: str = None, valor: float = None, descricao: str = None):
    # Busca o produto
    produto = db.query(Produto).filter(Produto.id == produto_id).first()
    
    if not produto:
        return None # Ou apresentar erro

    # Atualiza somente os campos que foram enviados
    if nome:
        produto.nome = nome
    if valor:
        produto.valor = valor
    if descricao:
        produto.descricao = descricao

    # Salva as modificações
    db.commit()
    db.refresh(produto)
    return produto

# Wesley: função para buscar o produto pelo id
def buscar_produto_por_id(db: Session, produto_id: int):
    # Retorna o produto ou None se não existir
    return db.query(Produto).filter(Produto.id == produto_id).first()

# Julio: Função para atualizar o estoque do banco de dados
def atualizar_estoque(db: Session, produto_id: int, quantidade_vendida: int):
    produto = db.query(Produto).filter(Produto.id == produto_id).first()
    
    if not produto:
        raise ValueError("Produto não encontrado")
    
    if produto.quantidade < quantidade_vendida:
        raise ValueError("Estoque insuficiente")

    produto.quantidade -= quantidade_vendida
    
    db.commit()
    db.refresh(produto)
    return produto

# Julio: Função para buscar produtos pelo nome
def buscar_produtos_por_nome(db: Session, termo_busca: str):
    return db.query(Produto).filter(Produto.nome.ilike(f"%{termo_busca}%")).all()
