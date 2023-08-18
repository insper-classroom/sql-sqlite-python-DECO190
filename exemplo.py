import sqlite3

# https://www.devmedia.com.br/guia/guia-completo-de-sql/38314

# Conexão com o banco de dados dentro da pasta "db"
# A função connect() estabelece uma conexão com o banco de dados SQLite e retorna um objeto de conexão.
conn = sqlite3.connect('db/livros_database.db')

# Um cursor é um objeto que permite interagir com o banco de dados, 
# como executar instruções SQL e recuperar dados.
cursor = conn.cursor()

# Criar tabela de Livros
# Usamos o método execute() do cursor para executar instruções SQL.
# Neste caso, estamos criando uma tabela chamada Livros.
cursor.execute("""
CREATE TABLE IF NOT EXISTS Livros (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Titulo TEXT NOT NULL,
    Autor TEXT NOT NULL,
    AnoPublicacao INTEGER,
    Genero TEXT
);
""")

# Inserir registros de livros
# Preparamos uma lista de tuplas contendo os dados dos livros que queremos inserir.
livros = [
    ("O Senhor dos Anéis", "J.R.R. Tolkien", 1954, "Fantasia"),
    ("1984", "George Orwell", 1949, "Ficção Distópica"),
    ("Moby Dick", "Herman Melville", 1851, "Ficção")
]

# Usamos o método executemany() para inserir vários registros de uma vez.
# Ele toma uma consulta SQL e uma lista de tuplas como parâmetros.
cursor.executemany("""
INSERT INTO Livros (Titulo, Autor, AnoPublicacao, Genero)
VALUES (?, ?, ?, ?);
""", livros)

# Depois de fazer alterações no banco de dados, como inserir registros,
# precisamos confirmar essas alterações usando o método commit() do objeto de conexão.
conn.commit()

# Selecione e mostre todos os registros de livros
# Usamos o método execute() para executar uma consulta SELECT.
cursor.execute("SELECT * FROM Livros")

# O método fetchall() recupera todos os registros resultantes da consulta.
print(cursor.fetchall())

# Atualizar registro
# Usamos o método execute() para atualizar um registro no banco de dados.
cursor.execute("UPDATE Livros SET AnoPublicacao = ? WHERE Titulo = ?", (1950, "1984"))
conn.commit()

# Deletar registro
# Usamos o método execute() para deletar um registro do banco de dados.
cursor.execute("DELETE FROM Livros WHERE Titulo = ?", ("Moby Dick",))
conn.commit()

# Mostrando os registros após as operações de atualização e exclusão
cursor.execute("SELECT * FROM Livros")
print(cursor.fetchall())

# É importante fechar a conexão após terminar de interagir com o banco de dados.
# Isso libera os recursos e garante que todas as alterações pendentes sejam confirmadas.
conn.close()
