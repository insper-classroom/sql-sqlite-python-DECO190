import sqlite3

# Exercício de Python - Sqlite

# Conexão com o banco de dados dentro da pasta "db"
conn = sqlite3.connect('db/database_alunos.db')
cursor = conn.cursor()

# Vamos criar uma tabela chamada "Estudantes" com os seguintes campos:
# ID (chave primária) -  Criado automáticamente pela base de dados
# Nome
# Curso
# Ano de Ingresso


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
               

