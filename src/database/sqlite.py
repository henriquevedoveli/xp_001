import sqlite3

class SQliteHandler:
    def __init__(self) -> None:
        self.conn = sqlite3.connect('/sqlite/auditoria.db')

        self.cursor = self.conn.cursor()

        self.cursor.execute('''
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
        ''')


    def save_audit_data(self, model_name, valores, predict):
        self.cursor.execute('''
                INSERT INTO auditoria (
                    model_name, valor1, valor2, valor3, valor4, valor5, valor6, valor7, valor8, 
                    valor9, valor10, valor11, valor12, valor13, predict
                ) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (model_name, *valores, predict))

        self.conn.commit()

        self.conn.close()

