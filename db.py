import sqlite3

conn = sqlite3.connect("todo-app.db")

def criar_tabela_todo():
    cursor = conn.cursor()
    conn.execute("""
    CREATE TABLE IF NOT EXISTS tarefa (
        cd_tarefa integer primary key autoincrement,
        tarefa text,
        concluido integer
    )
        """)

def add_tarefa(tarefa):

    conn.execute("INSERT INTO tarefa (tarefa, concluido) VALUES (?, 0)", (tarefa, ))
    conn.commit()

def remover_tarefa(cd_tarefa):
    conn.execute("DELETE FROM tarefa where cd_tarefa = ? ", (cd_tarefa, ))
    conn.commit()

def concluir_tarefa(cd_tarefa):
    conn.execute("UPDATE tarefa SET concluido = 1 WHERE cd_taerfa = ?", (cd_tarefa, ))
    conn.commit()

def get_tarefas():
    return conn.execute("SELECT cd_tarefa, tarefa, concluido FROM tarefa")
    
