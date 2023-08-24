import sqlite3

conn = sqlite3.connect('db/database_alunos.sqlite3')
cursor = conn.cursor()

def create_table(name, columns): 
    cursor.execute(f"""
    CREATE TABLE IF NOT EXISTS {name} ({columns})
    """)

    conn.commit()

def insert(table, columns, data):
    cursor.executemany(f"""
    INSERT INTO {table} ({", ".join(columns)}) VALUES ({", ".join(["?"] * len(columns))});
    """, data)

    conn.commit()

def select(table, columns: [], limit="-1"):
    cursor.execute(f"""SELECT {", ".join(columns)} FROM {table} LIMIT {limit}""")

    res = cursor.fetchall()

    return res

def select_where(table, columns: [], condition: str):
    cursor.execute(f"""SELECT {", ".join(columns)} FROM {table} WHERE {condition}""")

    res = cursor.fetchall()

    return res

def update(table, column, new_value, condition):
    cursor.execute(f"UPDATE {table} SET {column} = {new_value} WHERE {condition}")
    conn.commit()

def update_all(table, column, new_value, condition=""):
    cursor.execute(f"UPDATE {table} SET {column} = {new_value}")
    conn.commit()

def delete_by_id(table, id):
    cursor.execute(f"DELETE FROM {table} WHERE ID = {id}")
    conn.commit()