from infra.db import con
from wrap_connection import transact 
from model.pedido import Pedido

sql_criar = "INSERT INTO PEDIDO(nome,cpf, CEP,RUA,BAIRRO,NUMERO,EMAIL,TELEFONE,SABORPIZZA,QUANTIDADE_PIZZA,FORMA_PAGAMENTO,VALOR_TOTAL) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)"

@transact(con)
def criar(pedido):
    cursor.execute(sql_criar, (pedido.nome,pedido.cpf,pedido.cep, pedido.rua,pedido.bairro,pedido.numero,pedido.email,pedido.telefone,pedido.saborpizza,pedido.quantidadePizza,pedido.formaPagamento,pedido.valorTotal))
    connection.commit()


