import sqlite3

#CRIAR A CLASSE QUE VAI SER RESPONSÁVEL PELO BANCO DE DADOS
class ConectarDB(object):
#MÉTODO CONSTRUTOR QUE FAZ A CONEXÃO COM O BANCO
    def __init__(self):
        self.conn = sqlite3.connect("todo-app.db")
        self.cursor = self.conn.cursor()
        self.criar_tabela()

#MÉTODO QUE CRIA A TABELA
    def criar_tabela(self):
        try:
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tarefa (
                cd_tarefa integer primary key autoincrement,
                tarefa text,
                concluido text
            )
                """)
        except Exception as e:
            print('[x] Falha ao criar tabela %s [x]' %e)
        else: 
            print('\n[!] Tabela criada com sucesso [!]\n')

#MÉTODO QUE ADICIONA A TAREFA
    def add_tarefa(self, tarefa):

        self.conn.execute("INSERT INTO tarefa (tarefa, concluido) VALUES (?, 'PENDENTE')", (tarefa, ))
        self.conn.commit()
#MÉTODO QUE REMOVE A TAREFA DE ACORDO COM O ROWID
    def remover_tarefa(self, rowid):
        self.conn.execute("DELETE FROM tarefa where rowid = ? ", (rowid, ))
        self.conn.commit()
#MÉTODO QUE CONCLUÍ A TAREFA DE ACORDO COM O ROWID
    def concluir_tarefa(self, cd_tarefa):
        self.conn.execute("UPDATE tarefa SET concluido = 'CONCLUÍDA' WHERE cd_tarefa = ?", (cd_tarefa, ))
        self.conn.commit()
#MÉTODO QUE FAZ A CONSULTA NA TABELA DE FORMA A EXIBIR TODOS OS DADOS NO GRID
    def consultar_tarefas(self):
        return self.conn.execute("SELECT rowid, * FROM tarefa").fetchall()
#MÉTODO QUE FAZ A CONSULTA NA TABELA DE FORMA A EXIBIR O ÚLTIMO DADO A SER INSERIDO
    def consultar_ultimo_rowid(self):
        return self.conn.execute("SELECT MAX(rowid) FROM tarefa").fetchone()
    
