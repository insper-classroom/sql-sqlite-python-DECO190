from db.db_utils import *

create_table("Estudantes", """
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Curso TEXT NOT NULL,
    AnoIngresso INTEGER
""")


# ============================================================================== 01
# students = [
#     ("Ana Silva", "Computação", 2019),
#     ("Pedro Mendes", "Física", 2021),
#     ("Carla Souza", "Computação", 2020),
#     ("João Alves", "Matemática", 2018),
#     ("Maria Oliveira", "Química", 2022),
# ]

# insert("Estudantes", ["Nome", "Curso", "AnoIngresso"], students)


# ============================================================================== 02
# print(select_where("Estudantes", ["*"], "AnoIngresso in (2019, 2020)"))


# ============================================================================== 03
# update("Estudantes", "AnoIngresso", "2005", "ID = 1")


# ============================================================================== 04
# delete_by_id("Estudantes", 1)


# ============================================================================== 05
# print(select_where("Estudantes", ["*"], "AnoIngresso > 2019"))


# ============================================================================== 06
# update_all("Estudantes", "AnoIngresso", "2018")