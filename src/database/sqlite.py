import sqlite3


class SQliteHandler:
    """
    Classe responsável por gerenciar a conexão e operações com o banco de dados SQLite,
    incluindo a criação da tabela de auditoria e o armazenamento de dados de predição.
    """

    def __init__(self) -> None:
        """
        Inicializa a conexão com o banco de dados SQLite e cria a tabela de auditoria, se ela não existir.
        """
        self.database_conn()

        self.cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS auditoria (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            model_name TEXT NOT NULL,
            valor1 REAL,
            valor2 REAL,
            valor3 REAL,
            valor4 REAL,
            valor5 REAL,
            valor6 REAL,
            valor7 REAL,
            valor8 REAL,
            valor9 REAL,
            valor10 REAL,
            valor11 REAL,
            valor12 REAL,
            valor13 REAL,
            predict INTEGER NOT NULL
        )
        """
        )

        self.database_commit_and_close_conn()

        

    def database_conn(self):
        self.conn = sqlite3.connect(
            "/sqlite/auditoria.db"
        )  
        self.cursor = self.conn.cursor()
        
    def database_commit_and_close_conn(self):
        self.conn.commit() 
        self.conn.close()

    def save_audit_data(self, model_name, valores, predict):
        """
        Insere os dados de auditoria no banco de dados após uma predição ser realizada.

        Parâmetros:
        model_name (str): O nome do modelo utilizado para a predição.
        valores (list): Lista contendo os valores de entrada utilizados para a predição.
        predict (int): O valor previsto pelo modelo.
        """

        self.database_conn()
        
        self.cursor.execute(
            """
            INSERT INTO auditoria (
                model_name, valor1, valor2, valor3, valor4, valor5, valor6, valor7, valor8, 
                valor9, valor10, valor11, valor12, valor13, predict
            ) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
            (model_name, *valores, predict),
        )

        self.database_commit_and_close_conn()
