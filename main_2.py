from db.db_utils import *

create_table("Estudantes", """
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Curso TEXT NOT NULL,
    AnoIngresso INTEGER
""")


# ============================================================================== 01 - Descomentar código abaixo para executar individualmente
# students = [
#     ("Ana Silva", "Computação", 2019),
#     ("Pedro Mendes", "Física", 2021),
#     ("Carla Souza", "Computação", 2020),
#     ("João Alves", "Matemática", 2018),
#     ("Maria Oliveira", "Química", 2022),
# ]

# insert("Estudantes", ["Nome", "Curso", "AnoIngresso"], students)


# ============================================================================== 02 - Descomentar código abaixo para executar individualmente
# print(select_where("Estudantes", ["*"], "AnoIngresso in (2019, 2020)"))


# ============================================================================== 03 - Descomentar código abaixo para executar individualmente
# update("Estudantes", "AnoIngresso", "2005", "ID = 1")


# ============================================================================== 04 - Descomentar código abaixo para executar individualmente
# delete_by_id("Estudantes", 1)


# ============================================================================== 05 - Descomentar código abaixo para executar individualmente
# print(select_where("Estudantes", ["*"], "AnoIngresso > 2019"))


# ============================================================================== 06 - Descomentar código abaixo para executar individualmente
# update_all("Estudantes", "AnoIngresso", "2018")
# print(select("Estudantes", ["*"]))
