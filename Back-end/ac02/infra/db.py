import sqlite3

create_sql = [

"""
CREATE TABLE IF NOT EXISTS PEDIDO(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cpf TEXT,
    CEP TEXT NOT NULL,
    RUA TEXT NOT NULL,
    BAIRRO TEXT,
    NUMERO TEXT,
    EMAIL TEXT,
    TELEFONE TEXT,
    SABORPIZZA TEXT,
    QUANTIDADE_PIZZA INTENGER,
    FORMA_PAGAMENTO TEXT,
    VALOR_TOTAL REAL,
    STATUS_PEDIDO INTENGER DEFAULT 1
);
"""
]

from wrap_connection import transact


def con():
    return sqlite3.connect('lms.db')

@transact(con)
def criar_db():
    for script in create_sql:
        cursor.execute(script)
    connection.commit()
    