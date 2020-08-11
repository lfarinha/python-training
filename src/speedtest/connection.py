import pyodbc


class Connection:

    def __init__(self, server=None, database=None, user=None, password=None):
        try:
            connection = ("Driver={ODBC Driver 17 for SQL Server};"
                          f"Server={server};Database={database};UID={user};PWD={password}")
            self.cursor = pyodbc.connect(connection).cursor()
        except Exception as e:
            print('oops en la conexion')

    def select(self, query):
        try:
            return self.cursor.execute(query)
        except Exception as e:
            print('oops en el query')

    def execute(self, query):
        try:
            self.cursor.execute(query)
            self.cursor.commit()
        except Exception as e:
            print('oops en el query')
