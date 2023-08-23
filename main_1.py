import sqlite3

# Exercício de Python - Sqlite

# Conexão com o banco de dados dentro da pasta "db"
conn = sqlite3.connect('db/database_alunos.sqlite3')
cursor = conn.cursor()

# Vamos criar uma tabela chamada "Estudantes" com os seguintes campos:
# ID (chave primária) -  Criado automáticamente pela base de dados
# Nome
# Curso
# Ano de Ingresso

cursor = conn.cursor()

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS Estudantes (
#     ID INTEGER PRIMARY KEY AUTOINCREMENT,
#     Nome TEXT NOT NULL,
#     Curso TEXT NOT NULL,
#     AnoIngresso INTEGER
# );
# """)
# conn.commit()


# =================================================================================== 01
# students = [
#     ("Ana Silva", "Computação", 2019),
#     ("Pedro Mendes", "Física", 2021),
#     ("Carla Souza", "Computação", 2020),
#     ("João Alves", "Matemática", 2018),
#     ("Maria Oliveira", "Química", 2022),
# ]

# cursor.executemany("""
# INSERT INTO Estudantes (Nome, Curso, AnoIngresso)
# VALUES (?, ?, ?);
# """, students)
# conn.commit()


# =================================================================================== 02
# cursor.execute("SELECT * FROM Estudantes WHERE AnoIngresso in (2019, 2020);")
# print(cursor.fetchall())


# =================================================================================== 03
# cursor.execute("UPDATE Estudantes SET AnoIngresso = ? WHERE nome = ?", (2005, "Ana Silva"))
# conn.commit()


# =================================================================================== 04
# cursor.execute("DELETE FROM Estudantes WHERE ID = ?", ("2"))
# conn.commit()


# =================================================================================== 05
# cursor.execute("SELECT * FROM Estudantes WHERE AnoIngresso > 2019")
# print(cursor.fetchall())


# =================================================================================== 06
# cursor.execute("UPDATE Estudantes SET AnoIngresso = 2018")
# conn.commit()

# cursor.execute("SELECT * FROM Estudantes;")
# print(cursor.fetchall())